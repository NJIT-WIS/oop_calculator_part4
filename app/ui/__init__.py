"""User interface for commandline"""


class UserInput:
    """User Input Class"""

    @staticmethod
    def ask_user_once(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def ask_user_until_exit(prompt: str) -> tuple:
        exit_commands = ('quit', 'done', 'stop')
        response = None
        user_responses = list()
        while response not in exit_commands:
            response = input(prompt)
            user_responses.append(response)
        return tuple(user_responses)


class UserInterfaceOutput:
    """User Input Class"""

    @staticmethod
    def tell_user(message: str):
        print(message)
