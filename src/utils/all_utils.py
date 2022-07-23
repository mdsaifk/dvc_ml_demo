import yaml
import os

# cc = "dvc_ML//config//config.yaml"
def read_yaml(path_of_yaml: str) -> dict:
    with open(path_of_yaml) as yaml_file:
        content = yaml.safe_load_all(yaml_file)
    
    return content