#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tsdao.ts_base import ts_base
import tushare as ts


# 通用行情接口
# 更新时间：股票和指数通常在15点～17点之间，数字货币实时更新，具体请参考各接口文档明细。
# 描述：目前整合了股票（未复权、前复权、后复权）、指数、数字货币、ETF基金、期货、期权的行情数据，未来还将整合包括外汇在内的所有交易行情数据，同时提供分钟数据。
# 其它：由于本接口是集成接口，在SDK层做了一些逻辑处理，目前暂时没法用http的方式调取通用行情接口。用户可以访问Tushare的Github，查看源代码完成类似功能。
class ts_pro_bar(ts_base):
    def __init__(self):
        super().__init__(self)
        #  接口  请求 api 名称
        self.api_name = "pro_bar"

    # 请求 所需要的  数据
    # 数据说明
    '''
    ----------------------------------------------------------------------
    输入参数

        名称	        类型	    必选	描述
        ts_code	    str	    Y	证券代码
        api	        str	    N	pro版api对象，如果初始化了set_token，此参数可以不需要
        start_date	str	    N	开始日期 (格式：YYYYMMDD，提取分钟数据请用2019-09-01 09:00:00这种格式)
        end_date	str	    N	结束日期 (格式：YYYYMMDD)
        asset	    str	    Y	资产类别：E股票 I沪深指数 C数字货币 FT期货 FD基金 O期权 CB可转债（v1.2.39），默认E
        adj	        str	    N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
        freq	    str	    Y	数据频度 ：支持分钟(min)/日(D)/周(W)/月(M)K线，其中1min表示1分钟（类推1/5/15/30/60分钟） ，默认D。对于分钟数据有600积分用户可以试用（请求2次），正式权限请在QQ群私信群主或积分管理员。
        ma	        list	N	均线，支持任意合理int数值。注：均线是动态计算，要设置一定时间范围才能获得相应的均线，比如5日均线，开始和结束日期参数跨度必须要超过5日。目前只支持单一个股票提取均线，即需要输入ts_code参数。
        factors	    list	N	股票因子（asset='E'有效）支持 tor换手率 vr量比
        adjfactor	str	    N	复权因子，在复权数据是，如果此参数为True，返回的数据中则带复权因子，默认为False。 该功能从1.2.33版本开始生效
        
    ----------------------------------------------------------------------
    输出参数

        具体输出的数据指标可参考各行情具体指标：

        股票Daily：https://tushare.pro/document/2?doc_id=27
        
        基金Daily：https://tushare.pro/document/2?doc_id=127
        
        期货Daily：https://tushare.pro/document/2?doc_id=138
        
        期权Daily：https://tushare.pro/document/2?doc_id=159
        
        指数Daily：https://tushare.pro/document/2?doc_id=95
        
        数字货币：https://tushare.pro/document/41?doc_id=4
    '''

    #  请求数据
    #  子类没有指定 api_name接口的话 可以继承重写
    def query(self):
        self.df = ts.pro_bar(**self.input_arr)

    # 子类继承 当前接口
    #  设置  请求参数
    def set_query_param(self):
        #  获取 数据 字段  字段用逗号连接  如: 'ts_code,symbol,name'
        self.fields = ''
        #  请求参数
        self.input_arr = {
            'ts_code': '000001.SZ',
            'adj': 'qfq',
            'start_date': '20200101',
        }
