from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from textSummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from textSummarizer.pipeline.model_train_pipeline import ModelTrainingPipeline
from textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME  = "Data Ingestion Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e


STAGE_NAME = "Data Transformation Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e


STAGE_NAME = "Model Train Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_train = ModelTrainingPipeline()
   model_train.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e