import decimal
import platform
import sys

from input_utilities import InputUtils


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


def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)
    # verify_yes_no_popup_works()
    # verify_get_single_choice_from_list_works()
    # verify_get_floating_point_number_works()
    # verify_get_decimal_number_works()
    verify_get_whole_number_works()


if __name__ == '__main__':
    main()
