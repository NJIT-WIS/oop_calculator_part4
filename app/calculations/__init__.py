"""Calculation abstract class and concrete operations"""
from app.operations import *


class Calculation:
    """My abstract Base Calculation Class"""

    # Class Properties should get Getter and Setter

    @classmethod
    def create(cls, val1, val2):
        """Factory Method"""
        return cls(val1, val2)

    def __init__(self, val1, val2):
        """This is the base class constructor"""
        self.val1 = val1
        self.val2 = val2

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result

    def set_val1(self, val1):
        """Get the result of a calculation"""
        self.val1 = val1

    def set_val2(self, val2):
        """Get the result of a calculation"""
        self.val2 = val2

    def get_val1(self):
        """Get the result of a calculation"""
        return self.val1

    def get_val2(self):
        """Get the result of a calculation"""
        return self.val2


class Addition(Calculation):
    """My Addition Concrete Calculation Class"""

    def get_result(self):
        return addition(self.val1, self.val2)


class Subtraction(Calculation):
    """My Subtraction Concrete Calculation Class"""

    def get_result(self):
        return subtraction(self.val1, self.val2)


class Division(Calculation):
    """My Division Concrete Calculation Class"""

    def get_result(self):
        return division(self.val1, self.val2)


class Multiplication(Calculation):
    """My Multiplication Concrete Calculation Class"""

    def get_result(self):
        return multiplication(self.val1, self.val2)
