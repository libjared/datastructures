#!/usr/bin/env python3

"""
how many random uint32s are generated before two equal numbers are generated in a row?
"""

import random

def main():
    gen = 2
    a, b = rand(), rand()
    while a != b:
        a, b = b, rand()
        gen += 2
    print("at generation={}, a={} and b={}".format(gen, a, b))

def rand():
    return random.randint(0, 0xFFFFFFFF)

if __name__ == "__main__":
    main()
