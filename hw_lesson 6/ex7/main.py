#! /usr/local/bin/python3

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    return factorial2(n - 2) * n
    

for i in range(10):
    print(factorial2(i))

