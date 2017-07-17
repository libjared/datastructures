#!/usr/bin/env python3

"""
https://leetcode.com/submissions/detail/109874510/
A seemingly open-ended yet actually very specific challenge to implement atoi.
"""

class Solution(object):
    def myAtoi(self, inp):
        """
        :type inp: str
        :rtype: int

        Possible special cases:
        Empty string
        Space string
        Negative numbers
        """

        strip_inp = inp.strip()
        if strip_inp == '':
            return 0

        if strip_inp[0] == '-':
            abs_inp = strip_inp[1:]
            negate = -1
        elif strip_inp[0] == '+':
            abs_inp = strip_inp[1:]
            negate = 1
        else:
            abs_inp = strip_inp
            negate = 1

        output = 0

        for c in abs_inp: # [1]234
            val_here = (ord(c) - ord('0'))
            if 0 <= val_here <= 9:
                output *= 10
                output += val_here
            else:
                break

        parsed = output * negate
        if parsed >= 2147483647:
            clamped = 2147483647
        elif parsed <= -2147483648:
            clamped = -2147483648
        else:
            clamped = parsed

        return clamped

