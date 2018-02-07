#!/usr/bin/env python

import logging
from os import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S')
hd=logging.StreamHandler(sys.stdout)
hd.setFormatter(formatter)
logger.addHandler(hd)
#logging.basicConfig(filename="app.log",level=logging.INFO)

logger.debug("hello debug")
logger.info("hello info")
logger.warn("hello warn")
logger.error("hello error")
logger.critical("hello critical")
