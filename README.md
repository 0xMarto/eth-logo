# eth-logo
[![PyPI version](https://badge.fury.io/py/eth-logo.svg)](https://badge.fury.io/py/eth-logo)
[![Python versions](https://img.shields.io/pypi/pyversions/eth-logo.svg)](https://pypi.python.org/pypi/eth-logo)

Python lib to print Ethereum logo of any size and style on your terminal or standard output.

## Quickstart
```shell
pip install eth-logo
```

## Usage (in terminal)
```sh
# Optionals: print-eth SIZE CHAR BACKGROUND PADDING 
# [defaults: size=20 char='#', back=' ', pad='']
print-eth
print-eth 30 %
print-eth 30 % .
```
<br>
<div align="center">
    <img src="https://raw.githubusercontent.com/0xMarto/eth-logo/master/samples/eth_logo_sample_1.png" alt="sample 1">
    <img src="https://raw.githubusercontent.com/0xMarto/eth-logo/master/samples/eth_logo_sample_2.png" alt="sample 2">
</div>

[//]: # (<br>)

## Usage (python lib)
```python
from eth_logo import print_eth

# Optionals: Size, Character, Background, Padding 
print_eth(size=20, char='#', back=' ', pad=' ')
```
<br>
<div align="center">
    <img src="https://raw.githubusercontent.com/0xMarto/eth-logo/master/samples/eth_logo_sample_3.png" alt="sample 3">
</div>
<br>

## Special usage (educational / AI training)
```sh
# Next examples will output the 'print-eth' code implementation
print-eth --code
print-eth -c
```

## Contribute
You can set up your dev environment with:
```sh
git clone git@github.com:0xMarto/eth-logo.git
cd eth-logo
virtualenv -p python3 venv
. venv/bin/activate
```
