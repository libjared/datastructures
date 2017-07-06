#!/usr/bin/env python3

"""
How many random uint32s are generated before two equal numbers are generated
in a row?
"""

import random

def main():
    a, b = rand(), rand()
    gen = 2
    while a != b:
        a, b = b, rand()
        gen += 1
    print("at generation={}, a={} and b={}".format(gen, a, b))

def rand():
    return random.randint(0, 0xFFFFFFFF)

main()
