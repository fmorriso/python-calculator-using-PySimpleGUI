import PySimpleGUI as sg
from PySimpleGUI import Window

from gui_scaling import GuiScaling
from gui_settings import GuiSettings


class OutputUtils():

    @staticmethod
    def get_scaled_size() -> (int, int):
        """get the scalesd size in the form of a tuple (width, height)."""
        scaling = GuiScaling(0.1)
        return scaling.scaled_width, scaling.scaled_height

    @staticmethod
    def display_message(msg: str, title: str) -> None:
        print(f'{OutputUtils.get_scaled_size()=}')
        print(msg)
        window_width_in_characters = max(int(len(msg)/2), 50)
        window_height_in_rows = max(int(len(msg)/10), 2)
        layout = [
            [sg.Text(
                text=msg,
                text_color = GuiSettings.text_color,
                background_color = GuiSettings.background_color,
                size = (window_width_in_characters, window_height_in_rows))
            ],
            [sg.Button(
                GuiSettings.button_OK,
                       button_color = (GuiSettings.button_color_foreground, GuiSettings.button_color_background)
            )],
        ]

        # Window
        scaled = GuiScaling(0.3333)
        window: Window = sg.Window(
            title = title,
            layout = layout,
            font = GuiSettings.font,
            background_color = GuiSettings.background_color,
            keep_on_top = True,
            size = (scaled.scaled_width, scaled.scaled_height),
            grab_anywhere = True,
            modal = True,
            scaling = False
            )

        # Event loop
        while True:
            event, values = window.read()
            if event in(GuiSettings.button_OK, sg.WIN_CLOSED):
                break
        window.close()

