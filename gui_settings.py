from enum import StrEnum, auto

class GuiSettings(StrEnum):
    """Store common GUI settings as enumerated constants."""
    background_color = '#00008B',
    button_color_foreground = '#00008B',
    button_color_background = '#FFFFFF',
    button_OK = 'Ok',
    button_CANCEL = 'Cancel',
    combo_selection_key = 'idx'
    font = '"Courier New" 16 bold',
    text_color='#FFFFFF'

