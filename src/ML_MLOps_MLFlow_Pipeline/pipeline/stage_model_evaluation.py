from src.ML_MLOps_MLFlow_Pipeline.config.configuration import ConfigurationManager
from src.ML_MLOps_MLFlow_Pipeline.components.model_evaluation import ModelEvaluation
from src.ML_MLOps_MLFlow_Pipeline.components.model_trainer import ModelTrainer
from src.ML_MLOps_MLFlow_Pipeline import logger


STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_in_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
