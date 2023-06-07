#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Ld = -(-number % 10)
else:
    Ld = number % 10
if Ld > 0:
    if Ld <= 6 and number != 0:
        print(f"Last digit of {number} is {Ld} and is less than 6 and not 0")
    elif Ld >= 5 and number != 0:
        print(f"Last digit of {number} is {Ld} and is greater than 5")
elif Ld < 0:
    print(f"Last digit of {number} is {Ld} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {Ld} and is 0")
