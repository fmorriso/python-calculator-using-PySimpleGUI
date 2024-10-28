import PySimpleGUI as sg

from gui_scaling import GuiScaling
from gui_settings import GuiSettings


class OutputUtils():

    @staticmethod
    def display_message(msg: str, title: str) -> None:
        # TODO: replace with custom window that can be sized using PyAutoGUI scaling
        sg.popup(
            msg,
            title=title,
            auto_close=False,
            modal = True,
            keep_on_top = True,
            font=GuiSettings.font,
            background_color=GuiSettings.background_color,
            text_color=GuiSettings.text_color,
            button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background),
            grab_anywhere = True
        )