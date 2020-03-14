#!/usr/bin/env python
# -*- coding: utf-8 -*-
from log.logger import logger


def main():
    print("Hello World!")

    log = logger()

    log.info("info .. ")
    log.debug("debug .. ")
    log.warning("warning .. ")
    log.error("error .. ")

if __name__ == '__main__':
    main()
