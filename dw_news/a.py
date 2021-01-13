from nb_log import LogManager

logger = LogManager('newdream').get_logger_and_add_handlers(40)

logger.debug('P1')
logger.info('P2')
logger.warning('P3')
logger.error('P4')
logger.critical('P5')
print('hello')