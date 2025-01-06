import PySimpleGUI as sg
from PySimpleGUI import Window

from gui_scaling import GuiScaling
from gui_settings import GuiSettings


class OutputUtils:

    @staticmethod
    def get_scaled_size() -> (int, int):
        """get the scaled size in the form of a tuple (width, height)."""
        scaling = GuiScaling(0.1)
        print(f'{scaling=}')
        return scaling.scaled_width, scaling.scaled_height

    @staticmethod
    def display_message(message: str, title: str) -> None:
        print(f'{OutputUtils.get_scaled_size()=}')
        print(message)
        window_width_in_characters = max(int(len(message) * 4), 50)
        print(f'{window_width_in_characters=}')
        window_height_in_rows = max(int(len(message) / 10), 2)
        layout = [
            [sg.Text(
                text=message,
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
        scaled = GuiScaling(0.333)
        window: Window = sg.Window(
            title = title,
            layout = layout,
            font = GuiSettings.font,
            background_color = GuiSettings.background_color,
            keep_on_top = True,
            size = (scaled.scaled_width, int(scaled.scaled_height / 2)),
            grab_anywhere = True,
            modal = True
            )

        # Event loop
        while True:
            event, values = window.read()
            if event in(GuiSettings.button_OK, sg.WIN_CLOSED):
                break
        window.close()

