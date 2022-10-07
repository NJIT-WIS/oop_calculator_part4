"""Calculation abstract class and concrete operations"""
from pprint import pprint

from app.operations import *


class Calculation(list):
    """My abstract Base Calculation Class"""

    @classmethod
    def create(cls, *argv):
        """Factory Method"""
        return cls(argv)

    def __init__(self, *argv):
        """This is the base class constructor"""
        super().__init__()
        if type(argv[0][0]) is not tuple:
            for value in argv[0]:
                self.append(value)
        else:
            for value in argv[0][0]:
                self.append(value)

    def __repr__(self):
        values = ', '.join(str(x) for x in self)
        return f'Calculation Type: {type(self)}, values: {values}, result={self.get_result()})'

    def get_result(self):
        pass


class Addition(Calculation):
    """My Addition Concrete Calculation Class"""

    def get_result(self):
        sum_of_values = 0.0
        for val in self:
            sum_of_values = addition(sum_of_values, val)
        return sum_of_values


class Subtraction(Calculation):
    """My Subtraction Concrete Calculation Class"""

    def get_result(self):
        difference_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            difference_of_values = subtraction(difference_of_values, val)
        return difference_of_values


class Division(Calculation):
    """My Division Concrete Calculation Class"""

    def get_result(self):
        quotient_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            quotient_of_values = division(quotient_of_values, val)
        return quotient_of_values


class Multiplication(Calculation):
    """My Multiplication Concrete Calculation Class"""

    def get_result(self):
        product_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            product_of_values = multiplication(product_of_values, val)
        return product_of_values
