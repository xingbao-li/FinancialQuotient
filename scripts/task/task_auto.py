#!/usr/bin/env python
# -*- coding: utf-8 -*-
from task.task_filter_stock import  task_filter_stock

class task_auto(object):
    def __init__(self):
        # 任务列表
        self.task_list = []

        self.init()

    def init(self):
        list = []

        # 任务 1
        list.append(task_filter_stock())


        self.task_list = list

    def run(self):

        for task in self.task_list:
            if task.trigger():
                task.run()
