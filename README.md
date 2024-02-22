# eth-logo
[//]: # ([![PyPI version]&#40;https://badge.fury.io/py/eth-account.svg&#41;]&#40;https://badge.fury.io/py/eth-logo&#41;)
[//]: # ([![Python versions]&#40;https://img.shields.io/pypi/pyversions/eth-account.svg&#41;]&#40;https://pypi.python.org/pypi/eth-logo&#41;)
Print Ethereum logo of any size on your stout.

## Quickstart
```sh
python3 -m pip install eth-logo
```

### Usage (in terminal)
```python
# Optionals: print-eth SIZE CHAR [defaults: size=20 char='#']
print-eth
print-eth 30 %
```

### Usage (in python)
```python
from eth_logo import print_eth

# Optionals: Size, Character, Background, Padding 
print_eth(size=20, char='#', back=' ', pad=' ')
```


### Contribute
You can set up your dev environment with:
```sh
git clone git@github.com:0xMarto/eth-logo.git
cd eth-logo
virtualenv -p python3 venv
. venv/bin/activate
```
