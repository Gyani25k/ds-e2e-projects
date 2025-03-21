from src.ds_e2e_project_1.constants import *
from src.ds_e2e_project_1.utils.common import *
from src.ds_e2e_project_1.entity.config_entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(self,config_filepath=Path('config/config.yaml'),params_filepath = Path('params.yaml'),
                schema_filepath = Path('schema.yaml')):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schemas = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir

        )

        return data_ingestion_config
