"""This is the main startup of the app"""
from ui import UserInput


def main():
    """This is the main function that is run"""
    op = UserInput.ask_user_once("What operation do you  want to  perform? ")
    values = UserInput.ask_user_until_exit("What are the values that you want to perform the operation on? Type a "
                                           "number and hit enter/return.  You can type done, exit, or quit when "
                                           "finished")


if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()
