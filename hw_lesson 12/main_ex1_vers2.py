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


class Calculator:

    operators = ('+', '-', '*', '/', '**')
    operation = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '**': lambda x, y: x ** y,
        '/': lambda x, y: x / y
    }

    def __init__(self) -> None:
        self.formula = None

    def validate_user_input(self, user_str: str):
        try:
            a, operator, b = user_str.split()
        except ValueError as e:
            raise InputFormulaError
        try:
            a, b = float(a), float(b)
        except Exception as e:
            raise InputNumberError
        if operator not in self.operators:
            raise InputOperatorError

        return a, operator, b


if __name__ == '__main__':
    calc = Calculator()
    while True:
        user_str = input()
        if user_str == 'quit':
            break
        else:
            a, operator, b = calc.validate_user_input(user_str)
            try:
                print(calc.operation[operator](a, b))
            except ArithmeticError as err:
                raise CalculationError
