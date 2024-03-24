import os
import sys
from logging import getLogger
from pathlib import Path

ROOT_DIR_PATH = Path(__file__).parent.parent.absolute()
sys.path.append(os.path.join(ROOT_DIR_PATH))
from src.common.configs import configs  # noqa
from src.common.logger import init_logger  # noqa

init_logger(configs.LOGGER_CONFIG_PATH)

logger = getLogger(__name__)

logger.info("Start root conftest.py")
