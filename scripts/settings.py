# -*- coding: utf-8 -*-
import os
import logging


APP_NAME = "FinancialQuotient"
APP_PATH = os.path.dirname(__file__)

# 日志
LOGS_PATH = os.path.join(APP_PATH, "logs")
LOGS_LEVEL = logging.DEBUG

# 数据库配置
DATABASE_CONFIG = {
    "read": {
        "host": "localhost",
        "port": "3306",
	    "db": "fq_center",
        "user": "root",
        "passwd": "lxb123456",
	    "charset": "utf8",
    }
}
