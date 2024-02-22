#!/usr/bin/python
"""
Usage:
    print-eth SIZE CHAR [defaults: size=20 char='#']

Examples:
    print-eth
    print-eth 30 %

Code:
    https://github.com/0xMarto/eth-logo
"""
import sys
from eth_logo import print_eth


def main():
    parameter_amount = len(sys.argv) - 1
    if parameter_amount == 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print(__doc__)
        sys.exit(1)
    try:
        if parameter_amount == 1:
            size = int(sys.argv[1])
            print_eth(size)
        elif parameter_amount == 2:
            size, char = int(sys.argv[1]), str(sys.argv[2])
            print_eth(size, char)
        else:
            print_eth()
    except Exception as e:
        print(e)
        sys.exit(1)


def print_eth_script():
    main()


if __name__ == "__main__":
    main()
