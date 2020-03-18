#!/usr/bin/env python
# -*- coding: utf-8 -*-
from init import log

from db.tssqlconn import TSDBObject
tsconn = TSDBObject()

import tushare as ts
tspro = ts.pro_api()

# 操作 基类
class ts_base(object):

    def __init__(self, api_name):
        #  接口  请求 api 名称
        self.api_name = None
        #  操作  数据类
        self.df = None
        #  初始化 api
        self.pro = tspro


        #  获取 数据 字段  字段用逗号连接  如: 'ts_code,symbol,name'
        self.fields = ''
        #  请求参数
        self.input_arr = {}

        self.set_query_param()

    #  请求数据
    #  子类没有指定 api_name接口的话 可以继承重写
    def query(self):
        self.df = self.pro.query(self.api_name, fields=self.fields, **self.input_arr)

    # 子类继承 当前接口
    #  设置  请求参数
    def set_query_param(self):
        pass

    # 保存到数据库
    def to_sql(self, if_exists='fail'):

        if self.df is not None:
            tsconn.to_sql(self.df, self.api_name, if_exists=if_exists)

    # 保存数据库
    def to_sql_replace(self):
        # Drop the table before inserting new values.
        # 插入新值之前，请先删除表。
        self.to_sql(if_exists='replace')

    # 保存数据库
    def to_sql_append(self):
        # Insert new values to the existing table.
        # 将新值插入现有表。
        self.to_sql(if_exists='append')
