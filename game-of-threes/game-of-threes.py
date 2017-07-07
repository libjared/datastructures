#!/usr/bin/env python3

"""
https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

Given a starting number, play the game of threes, printing your steps.
For every number, add 0, 1, or -1 to make it divisble by 3, then divide by 3.
Continue until you reach 1.
"""

def gameOfThrees(starting):
    num = starting
    while num > 1:
        choice = [0, -1, 1][num % 3]
        print("{} {}".format(num, choice))
        num += choice
        num //= 3
    print(1)

gameOfThrees(100)
