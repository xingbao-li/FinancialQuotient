# -*- coding: utf-8 -*-
import os
import logging


APP_NAME = "FinancialQuotient"
APP_PATH = os.path.dirname(__file__)

# 日志
LOGS_PATH = os.path.join(APP_PATH, "logs")
LOGS_LEVEL = logging.INFO#logging.DEBUG
