#!/usr/bin/env python3

"""
The first failed attempt at solving the problem. It would have been O(n) with
very little memory usage. It operated using a stack and the assumption that
the dictionary file was already sorted.

Since the dictionary is sorted, if you filter down to words (ending in any of
our four letters) and (have some specific length), all 4 solution words will be
right next to each other, in the order BGTY.
"""

# let phases = "BGTY"
# let stack = []
# loop each word:
#   if word ends in phases[0], push {phase:0, base:base} to stack. continue.
#   if word doesn't start with topstack.base, pop.
#
#   if word ends in phases[topstack.phase+1], topstack phase increment.
#   if topstack.phase == len(phases), break with solution.

phases = "bgty"
stack = []
with open("english.txt", "r") as f:
    for word in f:
        word = word.strip()
        if word[-1] == phases[0]:
            stack.append({'phase':0, 'base':word[:-1]})
            continue
        if len(stack) == 0:
            continue
        if not word.startswith(stack[-1]["base"]):
            stack.pop()
            continue
        currPhase = stack[-1]["phase"]
        
        if word[-1] == phases[currPhase + 1]:
            stack[-1]["phase"] += 1
        if stack[-1]["phase"] == len(phases) - 1:
            print(stack[-1]["base"])
            stack.pop()
