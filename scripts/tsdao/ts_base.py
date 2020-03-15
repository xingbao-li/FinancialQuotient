#!/usr/bin/env python
# -*- coding: utf-8 -*-
from init import log, tsconn, tspro

# 操作 基类
class ts_base():

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
    def query(self):
        self.df = self.pro.query(self.api_name, fields=self.fields, **self.input_arr)
        print(self.df)

    # 子类继承 当前接口
    #  设置  请求参数
    def set_query_param(self):
        pass

    # 保存到数据库
    def to_sql(self):

        if self.df is not None:
            pass
            #tsconn.to_sql(self.df, self.api_name)
