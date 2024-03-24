from logging import getLogger

from common.configs import configs
from common.logger import init_logger
from sub import sub_func

init_logger(configs.LOGGER_CONFIG_PATH)

logger = getLogger(__name__)


def main() -> None:
    logger.info("Start main")
    logger.info(f'{sub_func(text="Hello World!")=}')
    logger.info("End main")


if __name__ == "__main__":
    main()
