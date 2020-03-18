#!/usr/bin/env python
# -*- coding: utf-8 -*-
from init import log, auto

def main():
    log.info("========= 开始 执行任务 =========")

    # 执行任务
    auto.run()

    log.info("========= 结束 执行任务 =========")



if __name__ == '__main__':
    main()
