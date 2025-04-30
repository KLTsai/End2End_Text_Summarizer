from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
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
