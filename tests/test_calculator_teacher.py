"""Do not change these tests, they are meant to check your code and should fail"""

from app.calculator import Calculator


def test_calculator_operations():
    """Basic Calculator Tests using the Instance"""
    Calculator.add(2, 2)
    assert Calculator.history.get_last_result() == 4, "The Addition Function Failed"
    Calculator.divide(2, 2)
    assert Calculator.history.get_last_result() == 1, "The Division Function Failed"
    Calculator.multiply(2, 2)
    assert Calculator.history.get_last_result() == 4, "Multiplication Didn't work"
    Calculator.subtract(2, 2)
    assert Calculator.history.get_last_result() == 0, "Multiplication Didn't work"
