"""Custom Exception Classes"""


class OnlyOneValue(Exception):
    def __init__(self, message="Cannot Perform Operation On Only One Value"):
        super().__init__(self.message)
        self.message = message
