#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from settings import DATABASE_CONFIG as MYSQL_DATABASES

class TSDBObject(object):

    def __init__(self, db_key='read', database=None):
        dbconfig = MYSQL_DATABASES[db_key]
        self.database = database
        self.__connect(dbconfig)

    def __connect(self, dbconfig):
        host = dbconfig.get("host")
        user = dbconfig.get("user")
        passwd = dbconfig.get('passwd')
        port = int(dbconfig.get('port',3306))
        charset = dbconfig.get('charset', 'utf8')
        timeout = dbconfig.get('connect_timeout', 10)
        database = self.database or dbconfig.get('db')

        dbstr = 'mysql://%s:%s@%s/%s?charset=utf8' % (user, passwd, host, database)

        # 创建一个 db engine
        db = create_engine(dbstr)

        self.db = db

    '''
    if_exists: {'fail', 'replace', 'append'}, default 'fail'
    '''
    def to_sql(self, data, table, if_exists="fail"):
        data.to_sql(table, self.db, if_exists=if_exists)

