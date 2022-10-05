"""History class that extends the built-in list data structure type"""
from app.calculations import Calculation


class History(list):
    """This initialized the history object and calls  the list super init and addess any calculations passed"""
    def __init__(self, *argv):
        super().__init__()
        for arg in argv:
            self.append(arg)

    def get_last_result(self):
        return self[-1].get_result()

    def print_history(self):
        for calculation in self:
            print(calculation)

