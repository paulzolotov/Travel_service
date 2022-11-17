#! /usr/local/bin/python3

c = (2, 24, 9, 0, 27, 3, 54, 200, 31, 144, 45)

a = tuple(filter((lambda y: y % 9 == 0), c))

print(a)

