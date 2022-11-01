#!/usr/bin/env python3

import sys

from src.gpt2 import *


def main():
    gpt2 = GPT2()
    gpt2.runme()

    return 0


if __name__ == '__main__':
    sys.exit(main())
