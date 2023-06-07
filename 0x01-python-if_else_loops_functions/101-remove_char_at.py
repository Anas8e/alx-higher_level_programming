#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    result = str[0:n]
    result += str[n+1:]
    return result
