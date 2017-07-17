#!/usr/bin/env python3

"""
https://leetcode.com/submissions/detail/109869481/
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        I - 1
        V - 5
        X - 10
        L - 50
        C - 100
        D - 500
        M - 1000

        Examples:
        6-7 (LX-VII)
        1-6-9-8 (M-DC-XC-VIII)
        9-9-0 (CM-)

        Each place (10/100/1000) will be broken down into a combination of 3 different roman numeral character types: 1x, 5x, and 10x.
        Each being a multiplier of the current place value (10/100/1000).

        The pattern for each place is simple and consistent enough to encode in a lookup table without hard-to-read logic.
        The only exception is numbers >=4000: MMMM
        """

        roman = ['IVX', 'XLC', 'CDM', 'M??']
        decode = ['', '0', '00', '000', '01', '1', '10', '100', '1000', '02']

        output = ""
        instr = str(num)

        place = len(instr)
        for f in instr: # [1]698
            place -= 1
            here = int(f)

            decoder = decode[here]
            for g in decoder: # [1]00
                output += roman[place][int(g)]

        return output

