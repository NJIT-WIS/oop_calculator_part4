"""Calculator Class"""
from app.calculations import *
from app.history import History


class Calculator:
    """Improved Calculator with Class Methods and using the calculation history static prop instance"""
    # this is  a static history property holding our history list class
    history = History()

    @classmethod
    def add(cls, val1, val2):
        cls.history.append(Addition.create(val1, val2))
        return cls.history.get_last_result()

    @staticmethod
    def divide(val1, val2):
        return Division.create(val1, val2).get_result()

    @staticmethod
    def multiply(val1, val2):
        return Multiplication.create(val1, val2).get_result()

    @staticmethod
    def subtract(val1, val2):
        return Subtraction.create(val1, val2).get_result()
