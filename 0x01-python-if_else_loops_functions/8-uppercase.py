#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return 1
    return 0


def uppercase(str):
    result = ""
    for i in str:
        if islower(i):
            result += chr(ord(i) - 32)
        else:
            result += i
    print('{}'.format(result))
