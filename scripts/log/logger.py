# -*- coding: utf-8 -*-
import os
import logging
import time

from settings import LOGS_PATH, LOGS_LEVEL
from logging.handlers import TimedRotatingFileHandler


class logger(object):
    def __init__(self, log_name=""):
        self.logger = logging.getLogger(log_name)

        # 设置输出等级
        LEVELS = {
            'NOTSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

        filename = log_name
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        if log_name == "":
            filename = '%s' % timestamp
        else:
            filename = '%s.%s' % (log_name, timestamp)

        # 创建文件目录
        logs_dir = LOGS_PATH
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改 log 保存位置
        log_file = "{0}/{1}.log".format(logs_dir, filename)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 日志每日轮换， 保存近三个月的日志
        time_handler = TimedRotatingFileHandler(filename=log_file, when='D', interval=1, backupCount=30)
        time_handler.setFormatter(fmt)

        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(LOGS_LEVEL)
        console.setFormatter(fmt)

        # 添加内容到日志句柄中
        self.logger.addHandler(time_handler)
        self.logger.addHandler(console)
        self.logger.setLevel(LOGS_LEVEL)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)


