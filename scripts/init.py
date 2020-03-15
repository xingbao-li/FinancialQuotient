# -*- coding: utf-8 -*-
from log.logger import logger
log = logger()

#from db.sqlconn import DBObject
#conn = DBObject()

from db.tssqlconn import TSDBObject
tsconn = TSDBObject()

import tushare as ts
tspro = ts.pro_api()
