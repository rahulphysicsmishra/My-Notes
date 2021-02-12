import  logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s- second, m- minute, h= hour, d- day, w-weekday(w0-monday, w1-tuesday), midnight
handler = TimedRotatingFileHandler('timed_test.log',when='s',interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hare Krishna')
    time.sleep(5)

