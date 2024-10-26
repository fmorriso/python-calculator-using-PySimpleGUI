import sys, platform
import PySimpleGUI as sg

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


# Press the green button in the gutter to run the script.
def verify_yes_no_popup_works():
    resp = sg.popup_yes_no( 'Do you want to exit?', title='Yes/No',
                            font='"Courier New" 20', keep_on_top=True, text_color='white',
                            button_color=('#00008B','white'), background_color='#00008B')
    print(f'{type(resp)=}, {resp=}')
    # if sg.popup_yes_no('Do you want to exit?') == 'Yes':
    #     exit()

def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)
    verify_yes_no_popup_works()


if __name__ == '__main__':
    main()
