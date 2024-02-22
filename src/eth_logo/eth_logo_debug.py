#!/usr/bin/python
"""
This a development file to test new features with no optimizations.
Focused on readability to test things before migration to `eth_logo_core.py`

Example:
> Size: 20
          #
         ###
        #####
       #######
      #########
     ###########
    #############
   ###############
  #################
 ###################
   ###############
 #    #########    #
  ###     #     ###
   ######   ######
    #############
     ###########
      #########
       #######
        #####
         ###
          #
> Printed size: (21, 19)

# TODO Make printed logo more accurate (losing top/bottom symetry)
#           #
#          ###
#         #####
#        #######
#       #########
#      ###########
#     #############
#    ###############
#   #################
#  ###################
#    ###############
#  #    #########    #
#   ###     #     ###
#     #####   #####
#       #########
#         #####
#           #
"""

# Only for debug
DEFAULT = 21
input_size = int(input('\n> Size: ') or DEFAULT)
SIZE = input_size
HASH = '#'
SPACE = ' '
GAP = ' '
PAD = ' '

# Calculate sizes (applying min resolution limit and rounding)
height = max((SIZE // 3) * 3, 15)  # Size: 15 is the smallest
height = height + 2 if height % 2 == 0 else height - 1
width = height - 1
top = height // 2
bottom = height // 3
middle = height - top - bottom
print(f'> height: {height + 1}, top: {top}, mid: {middle}\n')  # Only for debug

for i in range(0, top):
    hashes = HASH * (2 * i + 1)
    spaces = SPACE * (top - i - 1)
    # print(spaces + hashes + spaces)
    print(PAD + spaces + hashes + spaces, f' | i: {i}, end: {top}')  # Only for debug

for i in range(top, top + middle):
    x = i - top
    if x == 0:
        side_hashes = HASH * 0
        gap = GAP * 2
        mid_hashes = HASH * (2 * i - 5)
    elif x < middle - 2:
        side_hashes = HASH * (x * 2 - 1)
        gap = GAP * 4
        mid_hashes = HASH * ((2 * i - 5) - (8 * x))
    elif x == middle - 2:
        side_hashes = HASH * (x * 2 - 1)
        gap = GAP * 5
        mid_hashes = HASH
    else:
        # Case: x == middle - 1 (last)
        side_hashes = HASH * (x * 2)
        gap = GAP * 1
        mid_hashes = gap
        # Next version test code
        # spaces = SPACE * x

    hashes = side_hashes + gap + mid_hashes + gap + side_hashes
    spaces = SPACE * (x - 1)
    # print(spaces + hashes + spaces)
    print(PAD + spaces + hashes + spaces, f' | i: {i}, end: {top + middle}, x: {x}')  # Only for debug

for i in range(top + middle, height + 1):
    # Next version test code
    # if i % 2 != 0 or i == top + middle:
    #     continue

    hashes = HASH * (2 * (height - i) + 1)
    spaces = SPACE * (i - top - 1)
    # print(spaces + hashes + spaces)
    print(PAD + spaces + hashes + spaces, f' | i: {i}, end: {height + 1}')  # Only for debug


def get_logo_size(size):
    _height = max((size // 3) * 3, 15)
    _height = _height + 2 if _height % 2 == 0 else _height - 1
    _width = _height - 1
    return _height + 1, _width
