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
