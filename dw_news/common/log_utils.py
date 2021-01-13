#coding:utf-8

import logging
import os
from logging import handlers

log_path = os.path.join(os.path.dirname(__file__),'..','logs')


class LogUtils:
    def __init__(self,log_path = log_path):
        self.log_file_name = 'log.log'
        self.logger = logging.getLogger('DWTT_API')
        self.logger.setLevel(10)



        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(10)

        file_handler = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),
                                                         when='D',
                                                         interval=1,
                                                         backupCount=7)

        file_handler.setFormatter(formatter)
        file_handler.setLevel(10)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()
        file_handler.close()

    def get_logger(self):
        # self.logger.debug('newdream')
        return self.logger

if __name__ == '__main__':
    log_ger = LogUtils().get_logger()
    log_ger.info('111newdream')