import os
from logging.config import dictConfig

import yaml

is_ci_environment = os.getenv("CI", "false") == "true"


def init_logger(logger_config_path: str) -> None:
    with open(logger_config_path, "r") as f:
        config = yaml.safe_load(f.read())

    # CI環境ではファイルハンドラーを除外
    if is_ci_environment:
        # filename属性を持たないハンドラーのみを保持
        config["handlers"] = {
            key: val
            for key, val in config["handlers"].items()
            if not val.get("filename")
        }
        # 更新されたハンドラーリストを基に各loggerのhandlersを更新
        for logger in config["loggers"].values():
            logger["handlers"] = [
                h for h in logger["handlers"] if h in config["handlers"]
            ]
        # root loggerのhandlersも更新
        config["root"]["handlers"] = [
            h for h in config["root"]["handlers"] if h in config["handlers"]
        ]

    dictConfig(config)
