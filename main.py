from src.ML_MLOps_MLFlow_Pipeline import logger
from src.ML_MLOps_MLFlow_Pipeline.pipeline.stage_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.ML_MLOps_MLFlow_Pipeline.pipeline.stage_data_validation import (
    DataValidationTrainingPipeline,
)
from src.ML_MLOps_MLFlow_Pipeline.pipeline.stage_data_transformation import (
    DataTransformationTrainingPipeline,
)
from src.ML_MLOps_MLFlow_Pipeline.pipeline.stage_model_training import (
    ModelTrainingPipeline,
)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
