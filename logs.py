import logging as log


# creating logger
logger = log.getLogger(__name__)
logger.setLevel(log.DEBUG)

# creating console handler and set level to debug
consol_handler = log.FileHandler('sample_log_file.log')
consol_handler.setLevel(log.DEBUG)

# create formatter
formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to console handler
consol_handler.setFormatter(formatter)
# add console handler to logger
logger.addHandler(consol_handler)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
