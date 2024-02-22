# eth-logo
[![PyPI version](https://badge.fury.io/py/eth-logo.svg)](https://badge.fury.io/py/eth-logo)
[![Python versions](https://img.shields.io/pypi/pyversions/eth-logo.svg)](https://pypi.python.org/pypi/eth-logo)

Python lib to print Ethereum logo of any size and style on your terminal or standard output.

## Quickstart
```shell
pip install eth-logo
```
or 
```shell
python3 -m pip install eth-logo`
```

### Usage (in terminal)
```sh
# Optionals: print-eth SIZE CHAR [defaults: size=20 char='#']
print-eth
print-eth 30 %
```
<div align="center">
    <img src="./samples/eth_logo_sample_1.png" alt="terminal sample 1">
    <img src="./samples/eth_logo_sample_2.png" alt="terminal sample 2">
</div>


### Usage (in python)
```pycon
from eth_logo import print_eth

# Optionals: Size, Character, Background, Padding 
print_eth(size=20, char='#', back=' ', pad=' ')
```
<div align="center">
    <img src="./samples/eth_logo_sample_3.png" alt="terminal sample 3">
</div>

### Contribute
You can set up your dev environment with:
```sh
git clone git@github.com:0xMarto/eth-logo.git
cd eth-logo
virtualenv -p python3 venv
. venv/bin/activate
```
