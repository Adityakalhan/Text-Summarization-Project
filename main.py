from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"
try :
    logger.info(f"\n\n>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=======================x")
except Exception as e :
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try :
    logger.info(f"\n\n>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"\n>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=======================x")
except Exception as e :
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try :
    logger.info(f"\n\n>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"\n>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=======================x")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try :
    logger.info(f"\n\n*****************************************************")
    logger.info(f"\n\n>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"\n>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=======================x")
except Exception as e :
    logger.exception(e)
    raise e