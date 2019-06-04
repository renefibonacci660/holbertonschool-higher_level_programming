#!/usr/bin/python3

for i in reversed(range(97, 123, 1)):
    print("{}".format(chr(i - 32))
          if not i % 2 == 0 else "{}".format(chr(i)), end="")
