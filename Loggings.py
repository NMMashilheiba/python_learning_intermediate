import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('C:\\Users\\ningt\Python_Intermediate\\logs\\timed_test_log.log', when='s', interval=4, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("hello, world!")
    time.sleep(4)
