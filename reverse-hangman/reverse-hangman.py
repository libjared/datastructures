#!/usr/bin/env python3

"""
A riddle goes:

- Add "g", and I may end early in the morning.
- Add "b", and I may end late in the afternoon.
- Add "t", and you better listen while you do it.
- Add "y", and it can come in a bundle.

The solution is to find a single set of letters that, with one added letter,
form words that are answers to those questions. The answer to this one is
"jo_" as in "jog/job/jot/joy". Of course this goes against the spirit of a
riddle, but why couldn't we use Python and a text dictionary to simplify our
search set down to just a few candidates?

Drawbacks:
- Memory usage. Have to store large chunk of dictionary in various data
structures.
- Time complexity. Python multiple set intersection isn't a clear-cut O(n), and
I am convinced an O(n) algorithm exists.

Advantages:
- Simplicity. Set intersection is handled by Python.
"""

phases = "bgty"
sets = {}

for c in phases:
    sets[c] = set()

with open("english.txt", "r") as f:
    for word in f:
        word = word.strip() # remove pesky \r\n
        last = word[-1] # the 'd' in 'word'
        base = word[:-1] # the 'wor' in 'word'
        if last in phases and len(base) > 0:
            sets[last].add(base)

all_sets = list(sets.values())
final = set.intersection(*all_sets)
print("Set of bases that end in {}".format(", ".join(phases)))
print(final)
