import colorlog

logger = colorlog.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

logger.debug('debug message')
logger.info('information message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
