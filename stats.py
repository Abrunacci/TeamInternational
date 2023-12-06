"""stats.py
This module contains the Stats class representation.
"""
from .decorators import input_is_valid, range_is_valid


class Stats:
    def __init__(self, data_capture):
        """
        :param data_capture:
            A list of integers [DataCapture.data].
        """
        self.data = data_capture

    @input_is_valid
    def less(self, number: int) -> int:
        """Stats.less
        This functions search all the lower than `number` values.

        :param number:
            An integer greater than 0 and lower than 1000.
        :return:
            Integer that represents the total of values lower than the input in self.data
        """
        lower_count = 0
        for i in self.data:
            if i < number:
                lower_count += 1
        return lower_count

    @range_is_valid
    def between(self, gte: int, lte: int) -> int:
        """Stats.between
        This functions search all the values between the two values passed in self.data

        :param gte:
            An integer greater than 0 and lower than 1000. Should be lower than lte.
        :param lte:
            An integer greater than 0 and lower than 1000. Should be greater than gte.

        :return:
            Integer that represents the total of values between gte and lte in self.data.
        """
        range_count = 0
        for i in self.data:
            if gte <= i <= lte:
                range_count += 1
        return range_count

    @input_is_valid
    def greater(self, number: int) -> int:
        """Stats.greater
            This functions search all the bigger than `number` values.

            :param number:
                An integer greater than 0 and lower than 1000.
            :return:
                Integer that represents the total of values greater than the input in self.data
        """
        greater_count = 0
        for i in self.data:
            if i > number:
                greater_count += 1
        return greater_count
