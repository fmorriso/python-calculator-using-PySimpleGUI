import decimal, sys
import PySimpleGUI as sg


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
        return True


    @staticmethod
    def get_single_choice(title: str, prompt: str, choices: list[str]) -> str:
        """get a single choice from a list of choices"""
        return choices[0]