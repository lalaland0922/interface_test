"""
@Time : 2021/7/17 21:42
@Author : ruslan
@Email : ruslan@163.com
@File : get_log.py
@Project : jrj_webAutoTest_26
@feature : 打印日志
@实现步骤：
"""
import logging


def print_log():
    logging.basicConfig(level=logging.INFO, format='%(name)s - %(asctime)s - %(filename)s - [line:%(lineno)d] - %('
                                                   'levelname)s: %(message)s')
    logger = logging.getLogger('jrj_webAutoTest_26')
    return logger


logger = print_log()

if __name__ == '__main__':
    logger.info('this is a info message.')