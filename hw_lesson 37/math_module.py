operators = ('+', '-', '*', '/', '**')

operation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
    '/': lambda x, y: x / y
}