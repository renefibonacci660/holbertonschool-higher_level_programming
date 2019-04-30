#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is " .format(number), end="")

neglast = number

if number < 0:
    number = number * -1

last = number % 10

if neglast < 0:
    last = last * -1

print("{} and is " .format(last), end="")

if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
