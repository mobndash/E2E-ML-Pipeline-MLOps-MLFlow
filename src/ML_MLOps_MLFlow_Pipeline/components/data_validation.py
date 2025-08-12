import os
from src.ML_MLOps_MLFlow_Pipeline import logger
from src.ML_MLOps_MLFlow_Pipeline.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e

    def validate_all_columns_datatype(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)

            dtype_mapping = {
                "int": ["int64", "Int64"],
                "float": ["float64", "Float64"],
                "object": ["object", "string"]
            }

            mismatches = []
            for col, expected_type in self.config.all_schema.items():
                actual_type = str(data[col].dtype)
                if actual_type not in dtype_mapping.get(expected_type, [expected_type]):
                    mismatches.append((col, expected_type, actual_type))

            validation_status = len(mismatches) == 0

            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Data Type validation status: {validation_status}\n")
                if mismatches:
                    f.write(f"Type mismatches: {mismatches}\n")

            return validation_status

        except Exception as e:
            raise e
