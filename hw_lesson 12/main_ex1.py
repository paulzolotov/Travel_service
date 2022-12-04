class InputFormulaError(Exception):
    """Исключение, генерирующееся в том случае, если
        входные данные не состоят из 3 действительных элементов"""
    pass


class InputNumberError(Exception):
    """Исключение, генерирующееся в том случае, если
        введенные a и b не являются действительными числами"""
    pass


class InputOperatorError(Exception):
    """Исключение, генерирующееся в том случае, если
        возникает ошибка при вычислении"""
    pass


class CalculationError(Exception):
    """Исключение, генерирующееся в том случае, если
        введенные a и b не являются действительными числами"""
    pass


def calculator() -> None:
    while True:
        try:
            user_str = input()
            if user_str == 'quit':
                break
            a, operator, b = user_str.split()
            a, b = map(float, (a, b))
            if operator not in ('+', '-', '*', '/', '**'):
                raise InputOperatorError('Второй элемент не соответствует поддерживаемым операторам (+,-,*,/,**)')
        except ValueError as vl:
            if 'could not convert string to float:' in vl.args[0]:
                raise InputNumberError('a и b должны быть действительными числами')
            if 'not enough values to unpack' in vl.args[0]:
                raise InputFormulaError('Неверный формат введенного выражения')
        else:
            try:
                if operator == '+':
                    print(a + b)
                elif operator == '-':
                    print(a - b)
                elif operator == '*':
                    print(a * b)
                elif operator == '**':
                    print(a ** b)
                elif operator == '/':
                    print(a / b)
            except ArithmeticError:
                raise CalculationError('Ошибка при вычислениях')
    return None


calculator()
