#!/usr/bin/env python3

"""
https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

Given a 5-character input of the format HH:MM, convert the 24-hour timestamp
into natural language.
"""

def timeFormatNatural(timestamp):
    output = ["It's"]
    # get components
    milHour = int(timestamp[:2])
    milMin = int(timestamp[3:5])
    # calculate hour
    HOUR_STR = ["twelve", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven"]
    output.append(HOUR_STR[milHour % 12])
    # calculate minute
    MIN_ONES_STR = [None, "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    MIN_TENS_STR = [None, None, "twenty", "thirty", "forty", "fifty"]
    if milMin == 0: # no output for minutes
        pass
    elif milMin <= 9: # oh x
        output.append("oh")
        output.append(MIN_ONES_STR[milMin])
    elif milMin <= 19: # ten, eleven, twelve, teens
        output.append(MIN_ONES_STR[milMin])
    else: # twenty to fifty nine
        output.append(MIN_TENS_STR[milMin // 10])
        onesPlace = milMin % 10
        if onesPlace != 0:
            output.append(MIN_ONES_STR[onesPlace])
    # calculate am/pm
    if milHour < 12:
        output.append("am")
    else:
        output.append("pm")
    return " ".join(output)

assert timeFormatNatural("00:00") == "It's twelve am"
assert timeFormatNatural("01:30") == "It's one thirty am"
assert timeFormatNatural("12:05") == "It's twelve oh five pm"
assert timeFormatNatural("14:01") == "It's two oh one pm"
assert timeFormatNatural("20:29") == "It's eight twenty nine pm"
assert timeFormatNatural("21:00") == "It's nine pm"
assert timeFormatNatural("14:12") == "It's two twelve pm"
print("All tests pass")
