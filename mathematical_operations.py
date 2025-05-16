from enum import StrEnum
from typing import Any

class MathOperation(StrEnum):
    addition= '+'
    subtraction= '-'
    multiplication= '*'
    division= '/'
    modulo= '%'

    @staticmethod
    def get_operations_list():
        lst: list[str] = []
        for operator in MathOperation:
            lst.append(f'{operator.value} {operator.name}')
        return lst


    def __str__(self):
        match self.value:
            case '+':
                return '+ Addition'
            case '-':
                return '- Subtraction'
            case '*':
                return '* Multiplication'
            case '/':
                return '/ Division'
            case '%':
                return '% Modulo'

        return None


    @staticmethod
    def from_string(val: str):
        """Convert a string to an instance of MathOperation"""
        match val[0]:
            case '+':
                return MathOperation.addition
            case '-':
                return MathOperation.subtraction
            case '*':
                return MathOperation.multiplication
            case '/':
                return MathOperation.division
            case '%':
                return MathOperation.modulo
        return None


