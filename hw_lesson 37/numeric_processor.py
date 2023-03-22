from Exceptions import *
from math_module import operators, operation


class NumericOperationProcessor:
    @staticmethod
    def calculator(data: str) -> str:
        """
        Execute numeric operation from given data and given there arguments
        Handles different exceptions (e.g. from format of data, wrong amount of parameters
        passed in string_command for specific command)
        :param data: string command to execute
        :return: string result or throwing an exception
        """
        try:
            a, operator, b = data.split()
        except ValueError as e:
            raise InputFormulaError('InputFormulaError')
        try:
            a, b = map(float, (a, b))
        except Exception as e:
            raise InputNumberError('InputNumberError')
        if operator not in operators:
            raise InputOperatorError('InputOperatorError')
        try:
            return str(operation[operator](a, b))
        except ArithmeticError:
            raise CalculationError('CalculationError')
