"""data_capture.py
This module contains the DataCapture class representation.
"""

from decorators import input_is_valid
from stats import Stats


class DataCapture:
    def __init__(self):
        self.data = []

    @input_is_valid
    def add(self, number: int) -> None:
        """
        This function takes an integer value and appends it to `self.data` list.
        If the input is invalid, it will not append the data.

        :param number:
            An integer greater than 0 and lower than 1000.
        :return:
            None
        """
        self.data.append(number)

    def build_stats(self) -> Stats:
        """
        This function builds and returns a Stats object.

        :return:
            Stats object
        """
        return Stats(self.data)
