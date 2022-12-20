#!/usr/bin/python3
def uppercase(str):
    stp1 = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            stp1 = stp1 + chr((ord(letter) - 32))
        else:
            stp1 = stp1 + letter
    print("{:s}".format(stp1))
