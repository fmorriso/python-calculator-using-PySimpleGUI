import decimal, sys
from decimal import Decimal
from typing import ClassVar

import PySimpleGUI as sg
from pygame.display import get_window_size

from gui_scaling import GuiScaling
from gui_settings import GuiSettings


class InputUtils:
    """A set of utilities for performing common input operations."""


    @staticmethod
    def get_scaled_size() -> (int, int):
        scaling = GuiScaling()
        return scaling.scaled_width, scaling.scaled_height


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
        waiting_for_valid_input = True
        number = Decimal('NaN')
        while waiting_for_valid_input:
            text = sg.popup_get_text(
                title = title,
                message = prompt,
                font = GuiSettings.font,
                grab_anywhere = True,
                keep_on_top = True,
                text_color = GuiSettings.text_color,
                button_color = (
                    GuiSettings.button_color_foreground, GuiSettings.button_color_background),
                background_color = GuiSettings.background_color,
                modal = True)
            try:
                number = float(text)
                waiting_for_valid_input = False
            except ValueError:
                sg.popup_quick_message('Invalid number - try again.', 'Invalid input', modal = True, auto_close = False )

        return number


    @staticmethod
    def get_yesno_response(title: str, question: str) -> bool:
        """get a yes/no (True/False) response to a question"""
        resp = sg.popup_yes_no(
            question,
            title = title,
            font = GuiSettings.font,
            grab_anywhere = True,
            keep_on_top = True,
            text_color = GuiSettings.text_color,
            button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background),
            background_color = GuiSettings.background_color,
            modal = True,
        )
        return resp.lower()[0] == 'y'


    @staticmethod
    def get_single_choice(title: str, prompt: str, choices: list[str]) -> str | None:
        """get a single choice from a list of choices"""
        layout = [
            [sg.Text(prompt, text_color = GuiSettings.text_color, background_color = GuiSettings.background_color)],
            [
                sg.Combo(
                    values = choices,
                    readonly = True,
                    key = GuiSettings.combo_selection_key,
                    default_value = choices[0],
                    text_color = GuiSettings.background_color,
                    background_color = GuiSettings.text_color,
                    font = GuiSettings.font
                )
            ],
            [
                sg.Button(GuiSettings.button_OK,
                          button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background)),
                sg.Button(GuiSettings.button_CANCEL,
                          button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background))
            ]
        ]
        window = sg.Window(
            title,
            layout,
            background_color = GuiSettings.background_color,
            button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background),
            font = GuiSettings.font,
            auto_size_text = True,
            keep_on_top = True,
            size = InputUtils.get_scaled_size(),
            grab_anywhere = True
        )
        choice = ''
        while True:
            event, values = window.read()
            match event:
                case GuiSettings.button_OK:
                    choice = values[GuiSettings.combo_selection_key]
                    break
                case _:
                    choice = ''
                    break

        window.close()
        return choice
