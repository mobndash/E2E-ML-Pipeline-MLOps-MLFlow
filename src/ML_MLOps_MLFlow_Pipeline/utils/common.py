import os
import sys
from src.ML_MLOps_MLFlow_Pipeline import logger
# from src.ML_MLOps_MLFlow_Pipeline.exception import CustomException
import yaml
from box.exceptions import BoxValueError
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import joblib


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox (like a dictionary but with dot access).
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create multiple directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at path : {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Saved JSON file at path : {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return its contents as a ConfigBox.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from path : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data to a binary file using joblib.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved binary file at path : {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load data from a binary file using joblib.
    """
    data = joblib.load(path)
    logger.info(f"Loaded binary file from path : {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
