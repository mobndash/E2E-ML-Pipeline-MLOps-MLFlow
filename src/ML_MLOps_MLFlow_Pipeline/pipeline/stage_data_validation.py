from src.ML_MLOps_MLFlow_Pipeline.config.configuration import ConfigurationManager
from src.ML_MLOps_MLFlow_Pipeline.components.data_validation import DataValiadtion
from src.ML_MLOps_MLFlow_Pipeline import logger


STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_columns_datatype()


if __name__ == '__main__':
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
