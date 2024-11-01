import platform
import sys

from input_utilities import InputUtils
from mathematical_operations import MathOperation
from output_utilities import OutputUtils


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_operation() -> MathOperation:
    """Prompt the user for a valid mathematical operation and return it as an enumerated value."""
    choices: list[str] = MathOperation.get_operations_list()
    opr = InputUtils.get_single_choice('Operation', 'Select an operation', choices)
    math_opr = MathOperation.from_string(opr)
    return math_opr


def perform_operation(num1, num2, operation: MathOperation):
    """Given two numbers and an operation, perform the operation and return the result."""
    match operation:
        case MathOperation.addition:
            return num1 + num2
        case MathOperation.subtraction:
            return num1 - num2
        case MathOperation.multiplication:
            return num1 * num2
        case MathOperation.division:
            return num1 / num2
        case MathOperation.modulo:
            return num1 % num2


def perform_one_calculation():
    """Perform a single calculation by prompting for two numbers, an operation to perform on those two numbers, and then displaying the result."""
    num1 = InputUtils.get_decimal_number('First', 'Enter the first number:')
    num2 = InputUtils.get_decimal_number('Second', 'Enter the second number:')
    operation: MathOperation = get_operation()
    result = perform_operation(num1, num2, operation)
    msg = f'{num1} {operation.value} {num2} = {float(result):.3f}'
    print(msg)
    OutputUtils.display_message(msg, 'Result')


def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)

    keep_calculating = True
    while keep_calculating:
        perform_one_calculation()
        keep_calculating = InputUtils.get_yesno_response('Keep Calculating?', "Perform another calculation?", )

    msg = 'Thank you for using my calculator'
    print(msg)
    OutputUtils.display_message(msg, 'Calculator')


if __name__ == '__main__':
    main()
