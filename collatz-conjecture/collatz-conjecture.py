#!/usr/bin/env python3

def collatz(starting):
    print("Collatz conjecture for {}:".format(starting))
    solution = []
    num = starting
    while True:
        solution.append(num)
        if num == 1:
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = num*3+1
    print(" ".join([str(x) for x in solution]))

collatz(44)
