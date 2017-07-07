#!/usr/bin/env python3

"""
Given a string containing only the characters in "([{}])",
write a function that returns a boolean stating whether all braces are
matching.

Corner cases:
- An empty expression is True.
- An unexpected end of stream (more opens than closes) is False.
- An unexpected pop from empty stack (more closes than opens) is False.

Overview of algorithm:
- Use a stack. Loop through each character.
- When you encounter an open brace, push it onto the stack.
- When you encounter a closed brace, pop off the stack and check that your
    closed and open braces are of the same type. If not, return False early.
- When you reach the end of your input string, the expression is balanced iff
    the stack is empty.
"""

def checkBraceMatch(strToCheck):
    stack = []
    for cha in strToCheck:
        #print("cha={}, stack={}".format(cha, stack))
        if cha in "({[": # its an open, push
            stack.append(cha)
        if cha in ")}]": # its a close, pop
            if len(stack) == 0: return False
            match = stack.pop()
            if match == "(" and cha != ")": return False
            if match == "{" and cha != "}": return False
            if match == "[" and cha != "]": return False
            # brace pair matches, we're ok so far
    return len(stack) == 0

# test cases

testA = checkBraceMatch("()(())([{}]){[]}") == True  # correct braces
testB = checkBraceMatch("()(())([{})){[]}") == False # incorrect braces
testC = checkBraceMatch("") == True
testD = checkBraceMatch("((()") == False
testE = checkBraceMatch("())") == False

if testA and testB and testC and testD and testE:
    print("Tests pass")
else:
    print("Tests fail");
