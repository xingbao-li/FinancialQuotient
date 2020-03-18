#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  筛选 数据股票

# 1. 主板(沪股通60， 深股通00)/中小板(002)  价格 < 30
# 2. 均线  处于上升状态
# 3. 公司经营状况
# 4. pb温度计
# 5. 换手率
from task.task_base import task_base
from init import log
# 使用库: pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。

class task_filter_stock(task_base):

    # 触发器
    def trigger(self):
        return True

    # 运行脚本
    def run(self):
        log.debug("==== 执行了 task_fiter_stock")
