#! /usr/local/bin/python3

def factorial2(n):
    if n <= 2:
        return n
    return factorial2(n - 2) * n
    

for i in range(10):
    print(factorial2(i))

