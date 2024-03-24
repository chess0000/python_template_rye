from logging import getLogger

logger = getLogger(__name__)


def sub_func(text: str) -> str:
    logger.info("sub_func")
    return f"sub_func: {text}"
