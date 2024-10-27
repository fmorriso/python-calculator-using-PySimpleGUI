import decimal, sys
import PySimpleGUI as sg

from gui_settings import GuiSettings


class InputUtils:

    @staticmethod
    def get_whole_number(title: str, prompt: str) -> int:
        """Get a whole number as directed by the specified prompt."""
        return 0


    @staticmethod
    def get_decimal_number(title: str, prompt: str) -> decimal.Decimal:
        """return a floating-point number as directed by the prompt"""
        min = 0
        max = decimal.MAX_EMAX
        decimals = sys.float_info.dig
        # code needed here
        return decimal.Decimal('0')


    @staticmethod
    def get_floating_point_number(title: str, prompt: str) -> float:
        return 0


    @staticmethod
    def get_yesno_response(title: str, question: str) -> bool:
        """get a yes/no (True/False) response to a question"""
        resp = sg.popup_yes_no(question, title=title,
                               font=GuiSettings.font, keep_on_top=True,
                               text_color=GuiSettings.text_color,
                               button_color=(GuiSettings.button_color_foreground, GuiSettings.button_color_background),
                               background_color=GuiSettings.background_color)
        return resp.lower()[0] == 'y'


    @staticmethod
    def get_single_choice(title: str, prompt: str, choices: list[str]) -> str:
        """get a single choice from a list of choices"""
        selection_key = 'idx'
        layout = [
            [sg.Text(prompt, text_color=GuiSettings.text_color, background_color=GuiSettings.background_color)],
            [sg.Combo(values=choices, readonly=True, key=selection_key, default_value=choices[0])],
            [sg.Button('Ok', button_color=(GuiSettings.button_color_foreground, GuiSettings.button_color_background))]
        ]
        window = sg.Window(title, layout, background_color=GuiSettings.background_color)
        while True:
            event, values = window.read()
            if event == GuiSettings.button_OK:
                return values[selection_key]

