import decimal
import platform
import sys

from input_utilities import InputUtils
from output_utilities import OutputUtils


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def verify_yes_no_popup_works():
    """Verify that yes/no question utility works correctly."""
    resp: bool = InputUtils.get_yesno_response('Exit?','Do you want to quit?')
    print(f'{type(resp)=}, {resp=}')


def verify_get_single_choice_from_list_works():
    choices: list[str] = ['Apple','Banana','Orange']
    choice = InputUtils.get_single_choice('Fruit Choice', 'Pick a fruit', choices)
    print(f'{type(choice)=}, {choice=}')


def verify_get_floating_point_number_works():
    n: float = InputUtils.get_floating_point_number('Deposit Amount','Enter deposit amount')
    print(f'{type(n)=}, {n=}')


def verify_get_decimal_number_works():
    n: decimal.Decimal = InputUtils.get_decimal_number(title='Radius', prompt =  'Enter radius')
    print(f'{type(n)=}, {n=}, {n*2=}')


def verify_get_whole_number_works():
    n: int = InputUtils.get_whole_number(title = 'Eggs', prompt = 'Enter number of eggs')
    print(f'{type(n)=}, {n=}, {n*2=}')

def get_operation() -> str:
    choices: list[str] = ['+', '-', '*', '/']
    opr = InputUtils.get_single_choice('Operation', 'Select an operation', choices)
    return opr
def perform_operation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2

def perform_one_calculation():
    num1 = InputUtils.get_decimal_number('First', 'Enter the first number:')
    num2 = InputUtils.get_decimal_number('Second', 'Enter the second number:')
    operation = get_operation()
    result = perform_operation(num1, num2, operation)
    msg = f'{num1} {operation} {num2} = {result}'
    print(msg)
    OutputUtils.display_message(msg, 'Result')

def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)
    # verify_yes_no_popup_works()
    # verify_get_single_choice_from_list_works()
    # verify_get_floating_point_number_works()
    # verify_get_decimal_number_works()
    # verify_get_whole_number_works()
    keep_calculating = True
    while keep_calculating:
        perform_one_calculation()
        keep_calculating = InputUtils.get_yesno_response('Keep Calculating?', "Perform another calculation?", )

    msg = 'Thank you for using my calculator'
    print(msg)
    OutputUtils.display_message(msg, 'Calculator')

if __name__ == '__main__':
    main()
