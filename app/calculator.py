"""Calculator Class"""
from app.calculations import *
from app.history import CalculationHistoryList as History


class Calculator:
    """Improved Calculator with Class Methods and using the calculation history static prop instance"""
    # this is  a static history property holding our history list class
    history = History()

    @classmethod
    def add(cls, *args):
        return cls.history.append(Addition.create(args))

    @classmethod
    def divide(cls, *args):
        return cls.history.append(Division.create(args))

    @classmethod
    def multiply(cls, *args):
        return cls.history.append(Multiplication.create(args))

    @classmethod
    def subtract(cls, *args):
        return cls.history.append(Subtraction.create(args))
