"""Calculator Class"""
from app.calculations import *
from app.history import CalculationHistoryList as History


class Calculator:
    """Improved Calculator with Class Methods and using the calculation history static prop instance"""
    # this is  a static history property holding our history list class
    history = History()

    @classmethod
    def add(cls, val1, val2):
        return cls.history.append(Addition.create(val1, val2))

    @classmethod
    def divide(cls, val1, val2):
        return cls.history.append(Division.create(val1, val2))

    @classmethod
    def multiply(cls, val1, val2):
        return cls.history.append(Multiplication.create(val1, val2))

    @classmethod
    def subtract(cls, val1, val2):
        return cls.history.append(Subtraction.create(val1, val2))
