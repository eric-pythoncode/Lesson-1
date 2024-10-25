testdict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2,
}

valuetocheck = 1

freq = list(testdict.values()).count(valuetocheck)

print("The value ", valuetocheck, " appears ", freq, " time(s) in the dictionairy.")