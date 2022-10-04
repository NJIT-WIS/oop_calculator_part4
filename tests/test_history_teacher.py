"""Do not change these tests, they are meant to check your code and should fail"""
from pprint import pprint

from app.calculations import Addition


def test_history_operations():
    """Basic History Tests using the Instance"""
    addition_instance = Addition(1, 2)
    assert isinstance(addition_instance, Addition), "Not an addition Instance"
    assert addition_instance.get_result() == 3, "Did not add 1 + 2 = 3"

    history = [addition_instance]

    assert isinstance(history[0], Addition)
    assert len(history) == 1
    history.clear()
    assert len(history) == 0
    addition_instance_1 = Addition(1, 1)
    addition_instance_2 = Addition(1, 2)
    addition_instance_3 = Addition(1, 3)
    history.append(addition_instance_1)
    history.append(addition_instance_2)
    history.append(addition_instance_3)
    assert len(history) == 3
    retrieve_instance = history.pop(-1)
    assert isinstance(retrieve_instance, Addition)
    assert len(history) == 2






