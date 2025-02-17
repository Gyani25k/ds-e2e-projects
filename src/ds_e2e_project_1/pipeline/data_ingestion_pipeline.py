from src.ds_e2e_project_1.config.configuration import ConfigurationManager
from src.ds_e2e_project_1.components.data_ingestion import DataIngestion
from src.ds_e2e_project_1 import logger


STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

