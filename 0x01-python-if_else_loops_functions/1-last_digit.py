#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if n > 5:
    print("Last digit of", number, "is", n, "and is greater than 5")
elif n < 6 and n != 0:
    print("Last digit of", number, "is", -1*n, "and is less than 6 and not 0")
elif n == 0:
    print("Last digit of", number, "is", n, "and is 0")