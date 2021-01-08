# import click
#
#
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

#

# def fu():
#     import logging.config
#
#     logging.config.fileConfig('logging.conf')
#     # create logger
#     logger = logging.getLogger('simpleExample')
#     # 'application' code
#     logger.debug('debug message')
#     logger.info('info message')
#     logger.warning('warn message')
#     logger.error('error message')
#     logger.critical('critical message')
"""
    import logging.config

    #  定义输出文件，默认输出到控制台
    logging.config.fileConfig('log.txt')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    logger.info('info log')
    logger.critical('critical info')
    logger.error('error message')
"""

# log_cli= 1
# log_cli_level = INFO
# log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
# log_cli_date_format=%Y-%m-%d %H:%M:%S

# log_file = log.txt
# log_file_level = DEBUG
# log_file_date_format = %Y-%m-%d-%H-%M-%S
# log_file_format = %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s



# if __name__ == '__main__':
#     import logging
#     import logging.config

    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.DEBUG)
    #
    # # create console handler and set level to debug
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    #
    # # create formatter
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    # # add formatter to ch
    # ch.setFormatter(formatter)
    #
    # # add ch to logger
    # logger.addHandler(ch)
    #
    # logger.info('info log')
    # logger.critical('critical info')
    # logger.error('error message')
    #
    # # create logger
    # logger = logging.getLogger('log.txt')
    # # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    #
    # logging.config.fileConfig('logging.conf')
    # # create logger
    # logger = logging.getLogger('log.txt')
    # # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')