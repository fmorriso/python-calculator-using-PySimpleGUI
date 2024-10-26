import sys, platform
import PySimpleGUI as sg

from gui_settings import GuiSettings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def verify_yes_no_popup_works():
    resp = sg.popup_yes_no( 'Do you want to exit?', title='Yes/No',
                            font=GuiSettings.font, keep_on_top=True,
                            text_color=GuiSettings.text_color,
                            button_color=(GuiSettings.button_color_foreground, GuiSettings.button_color_background),
                            background_color=GuiSettings.background_color)
    print(f'{type(resp)=}, {resp=}')
    # if sg.popup_yes_no('Do you want to exit?') == 'Yes':
    #     exit()

def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)
    verify_yes_no_popup_works()


if __name__ == '__main__':
    main()
