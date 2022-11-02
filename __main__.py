#!/usr/bin/env python3


import sys

from src.scrapper import Scrapper
from src.parser import Parser
from src.server import Server


# Error table
# 1 :: default error exit code
# 0 :: return successful exit code


def main():
    scrapper = Scrapper()
    parser = Parser()
    server = Server(scrapper, parser)
    rc = 1
    try:
        rc = server.start()
        rc = server.stop()
    except:
        return rc
    rc = 0
    return rc


if __name__ == '__main__':
    sys.exit(main())
