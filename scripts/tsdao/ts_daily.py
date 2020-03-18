#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tsdao.ts_base import ts_base


# 日线行情
# 数据说明： 交易日每天15点～16点之间。本接口是未复权行情，停牌期间不提供数据。
# 调取说明： 基础积分每分钟内最多调取500次，每次5000条数据，相当于23年历史，用户获得超过5000积分正常调取无频次限制。
# 描述： 获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据。
class ts_daily(ts_base):
    def __init__(self):
        super().__init__(self)
        #  接口  请求 api 名称
        self.api_name = "daily"

    # 请求 所需要的  数据
    # 数据说明
    '''
    ----------------------------------------------------------------------
    输入参数

        名称	        类型	    必选	    描述
        ts_code	    str	    N	    股票代码（支持多个股票同时提取，逗号分隔）
        trade_date	str	    N	    交易日期（YYYYMMDD）
        start_date	str	    N	    开始日期(YYYYMMDD)
        end_date	str	    N	    结束日期(YYYYMMDD)
        
    ----------------------------------------------------------------------
    输出参数

        名称	            类型	        描述
        ts_code	        str	        股票代码
        trade_date	    str	        交易日期
        open	        float	    开盘价
        high	        float	    最高价
        low	            float	    最低价
        close	        float	    收盘价
        pre_close	    float	    昨收价
        change	        float	    涨跌额
        pct_chg	        float	    涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
        vol	            float	    成交量 （手）
        amount	        float	    成交额 （千元）
    '''
    # 子类继承 当前接口
    #  设置  请求参数
    def set_query_param(self):
        #  获取 数据 字段  字段用逗号连接  如: 'ts_code,symbol,name'
        self.fields = ''
        #  请求参数
        self.input_arr = {
            'ts_code': '000001.SZ',
            'start_date': '20200101',
        }
