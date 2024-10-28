from enum import StrEnum, auto

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
            lst.append(operator.value)
        return lst
