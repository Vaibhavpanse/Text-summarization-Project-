from Text_Summarizer.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.logging import logger

STAGE_NAME = "Data Ingestion Steps"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e
