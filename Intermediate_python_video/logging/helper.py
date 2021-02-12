import logging
logger = logging.getLogger(__name__)
logger.propagate = False  # if false, it stops propagation of info msg to main....
logger.info('hello from helper')