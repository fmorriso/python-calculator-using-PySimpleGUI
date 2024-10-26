import sys, platform
import PySimpleGUI as sg

from gui_settings import GuiSettings
from input_utilities import InputUtils


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def verify_yes_no_popup_works():
    """Verify that yes/no question utility works correctly."""
    resp: bool = InputUtils.get_yesno_response('Exit?','Do you want to quit?')
    print(f'{type(resp)=}, {resp=}')


def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)
    verify_yes_no_popup_works()


if __name__ == '__main__':
    main()
