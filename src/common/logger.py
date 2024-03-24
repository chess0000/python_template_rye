from logging.config import dictConfig

import yaml


def init_logger(logger_config_path: str) -> None:
    with open(logger_config_path, "r") as f:
        config = yaml.safe_load(f.read())
        dictConfig(config)
