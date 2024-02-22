#!/usr/bin/python

def print_eth(size=20, char='#', back=' ', pad=' '):
    """
    Usage example: print_logo()

    :param size: logo height, could  be adjusted to fit proportions
    :param char: char to print each pixel of the logo
    :param back: char used to print each pixel of the background
    :param pad: string to print at the start of each line
    """
    height = max((size // 3) * 3, 15)
    height = height + 2 if height % 2 == 0 else height - 1
    top, bottom = height // 2, height // 3
    mid = height - (top + bottom)
    for i in range(height + 1):
        if i < top:
            hashes = char * (2 * i + 1)
        elif i < top + mid:
            x = i - top
            side = char * (x * 2 - 1 if x < mid - 1 else x * 2)
            aux = 2 if x == 0 else 1 if x == mid - 1 else 5 if x == mid - 2 else 4
            gap = back * aux
            aux = 2 * i - 5 - 8 * x
            core = char * aux if x < mid - 2 else char if x == mid - 2 else back
            hashes = side + gap + core + gap + side
        else:
            hashes = char * (2 * (height - i) + 1)
        spaces = back * (abs(i - top) - 1)
        print(pad + spaces + hashes + spaces)
