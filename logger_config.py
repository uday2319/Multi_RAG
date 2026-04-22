import logging
import os
def setup_logger():
    os.makedirs("logs",exist_ok=True)
    logger=logging.getLogger("rag_logger")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        file_handler =logging.FileHandler("logs/rag.log")
        formatter=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        file_handler.setFormatter(formatter) 
        logger.addHandler(file_handler)
    
    logger.propagate = False
    return logger
        

    
                 