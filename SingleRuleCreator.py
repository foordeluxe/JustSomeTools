#!/usr/bin/python
import string

inputString = input("Write the string to convert: ")
inputMethod = int(input("Write 0 for Append and 1 for Preppend: "))


def ruleAppend(text):
    alphanum = string.ascii_letters + string.digits
    multi = ""
    for chars in text:
        if chars not in alphanum:
            multi += "$\\x" + format(ord(chars), "x") + " "
        else:
            multi += "$" + chars + " "
    return multi[-len(multi):-1]


def rulePreppend(text):
    alphanum = string.ascii_letters + string.digits
    multi = ""
    text = text[::-1]
    for chars in text:
        if chars not in alphanum:
            multi += " ^\\x" + format(ord(chars), "x")
        else:
            multi += " ^" + chars
    return multi[-len(multi) + 1::]


if len(inputString) > 0:
    if inputMethod == 0:
        print(ruleAppend(inputString))
    elif inputMethod == 1:
        print(rulePreppend(inputString))
    else:
        print("Not a correct method")
else:
    print("There is no input string")