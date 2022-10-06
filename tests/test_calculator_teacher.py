"""Do not change these tests, they are meant to check your code and should fail"""

from app.calculator import Calculator


def test_calculator_operations():
    """Basic Calculator Tests using the Instance"""
    Calculator.add(2, 2, 2)
    assert Calculator.history.get_last_result() == 6, "The Addition Function Failed"
    Calculator.divide(2, 2, 2)
    assert Calculator.history.get_last_result() == .5, "The Division Function Failed"
    Calculator.multiply(2, 2, 2)
    assert Calculator.history.get_last_result() == 8, "Multiplication Didn't work"
    Calculator.subtract(2, 2, 2)
    assert Calculator.history.get_last_result() == -2, "Multiplication Didn't work"
