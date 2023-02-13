import os
import logging
import logging.handlers
from pathlib import Path

log_dir = os.path.normpath(os.path.expanduser('~/Documents/Claims BI Logs/'))
Path(log_dir).mkdir(parents=True, exist_ok=True)

def setup(name):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    log_fname = os.path.join(log_dir, name + '.log')
    rfh = logging.handlers.RotatingFileHandler(filename = log_fname,
                                                mode = 'a',
                                                maxBytes = 5*1024*1024,
                                                backupCount = 2,
                                                encoding = None,
                                                delay = 0)
    logger.addHandler(rfh)
    logging.basicConfig(format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname).4s | %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO,
                        handlers=[rfh, logging.StreamHandler()])
    return logger
