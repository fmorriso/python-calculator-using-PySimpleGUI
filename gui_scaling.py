import pyautogui


class GuiScaling:

    __screen_pct: float = 0.0

    @property
    def screen_pct(self):
        return self.__screen_pct

    __device_width: int = 0

    @property
    def device_width(self) -> int:
        return self.__device_width

    __device_height: int = 0

    @property
    def device_height(self) -> int:
        return self.__device_height

    __scaled_width: int = 0

    @property
    def scaled_width(self) -> int:
        return self.__scaled_width

    __scaled_height: int = 0

    @property
    def scaled_height(self) -> int:
        return self.__scaled_height

    def __init__(self, pct: float = 0.2, square: bool = False, multiple_of: int = 10):
        # calculate GUI size as a percentage of device screen size
        self.__device_width, self.__device_height = pyautogui.size()
        self.__screen_pct: float = float(pct)

        # round scaled width and height to multiple of 100 unless square needed in which case use height for both
        # since device height is usually the smaller of the two
        self.__scaled_height: int = int(
            (self.device_height * self.__screen_pct // multiple_of) * multiple_of)
        self.__scaled_width: int = self.scaled_height if square else int(
            (self.device_width * self.__screen_pct // multiple_of) * multiple_of)
