import logging
from pathlib import Path


def setup_logger():

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("research_rag")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(
            log_dir / "rag.log",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    logger.propagate = False

    return logger
