#!/usr/bin/python
"""
Usage:
    print-eth SIZE CHAR BACKGROUND PADDING
    [defaults: size=20 char='#' back=' ' pad=' ']

Examples:
    print-eth
    print-eth 30 %
    print-eth 30 % .
    print-eth --code

Sourcecode:
    https://github.com/0xMarto/eth-logo
"""
import sys
from eth_logo import print_eth, print_eth_code


def main():
    parameter_amount = len(sys.argv) - 1
    if parameter_amount == 1:
        if sys.argv[1] in ['-h', '--help']:
            print(__doc__)
            sys.exit(1)
        if sys.argv[1] in ['-c', '--code']:
            print_eth_code()
            sys.exit(1)
    try:
        if parameter_amount == 1:
            size = int(sys.argv[1])
            print_eth(size)
        elif parameter_amount == 2:
            size, char = int(sys.argv[1]), str(sys.argv[2])
            print_eth(size, char)
        elif parameter_amount == 3:
            size, char, back = int(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])
            print_eth(size, char, back)
        elif parameter_amount == 4:
            size, char, back, pad = int(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4])
            print_eth(size, char, back, pad)
        else:
            print_eth()
    except Exception as e:
        print(e)
        sys.exit(1)


def print_eth_script():
    main()


if __name__ == "__main__":
    main()
