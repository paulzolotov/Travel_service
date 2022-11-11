#! /usr/local/bin/python3

def get_digits(num: int) -> tuple:
    a = [int(i) for i in str(num)]
    return tuple(a)

a_t = get_digits(87178291199)
print(a_t)
