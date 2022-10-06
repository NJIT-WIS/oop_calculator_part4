"""Do not change these tests, they are meant to check your code and should fail"""
from pprint import pprint

from app.calculations import Addition, Multiplication
from app.history import CalculationHistoryList as History


def test_history_operations():
    """Basic History Tests using the Instance"""
    addition_instance = Addition.create(1, 2)
    assert isinstance(addition_instance, Addition), "Not an addition Instance"
    assert addition_instance.get_result() == 3, "Did not add 1 + 2 = 3"
    # Initializing a list
    addition_instance_1 = Addition.create(1, 2)
    history = History(addition_instance, addition_instance_1)
    # Checking that the first element of the array is an addition instance
    assert isinstance(history[0], Addition)
    # Check how many items are in the list
    assert len(history) == 2, "Did not have 1 element in the list"
    # Removes all the elements in the list
    history.clear()
    assert len(history) == 0, "Did not clear"
    addition_instance_1 = Addition.create(1, 1)
    addition_instance_2 = Addition.create(1, 2)
    addition_instance_3 = Addition.create(1, 3)
    # adding elements to existing list
    history.append(addition_instance_1)
    history.append(addition_instance_2)
    history.append(addition_instance_3)

    assert len(history) == 3, "There are not 3 elements in the list"
    # removing and loading an item in a list
    retrieve_instance = history.pop(-1)
    assert isinstance(retrieve_instance, Addition)
    assert len(history) == 2
    multiplication_instance1 = Multiplication.create(2, 8)
    history.append(multiplication_instance1)
    history.print_history()
