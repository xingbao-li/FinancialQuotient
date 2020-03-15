#!/usr/bin/env python
# -*- coding: utf-8 -*-
from init import log
from tsdao.ts_stock_basic import ts_stock_basic


def main():
    log.info("Hello World!")

    tsdb = ts_stock_basic()

    tsdb.query()
    tsdb.to_sql()



if __name__ == '__main__':
    main()
