from src.ML_MLOps_MLFlow_Pipeline.config.configuration import ConfigurationManager
from src.ML_MLOps_MLFlow_Pipeline.components.data_transformation import DataTransformation
from src.ML_MLOps_MLFlow_Pipeline import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            status_file_path = Path("artifacts/data_validation/status.txt")

            with open(status_file_path, "r") as f:
                statuses = f.readlines()

        # Check both validations
            schema_status = statuses[0].strip().split(":")[-1].strip()
            datatype_status = statuses[1].strip().split(":")[-1].strip()

            if schema_status == "True" and datatype_status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(
                    config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception(
                    "Your data schema or data types are not valid.")

        except Exception as e:
            print(e)
