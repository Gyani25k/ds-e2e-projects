from pathlib import Path
from box import ConfigBox 
import yaml
import os
from src.ds_e2e_project_1 import logger
from ensure import ensure_annotations

def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully Here is Content {content}")
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise ValueError("Yaml Fle is empy")

@ensure_annotations
def create_directories(path_to_directories:list , verbose = True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at path: {path}")