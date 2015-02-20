from sys import path
path.append('src')
from base import *


def except_first_spaces_test():
    text = '   fnao rqjp r   rjqp '
    assert(except_first_spaces(text) ==  'fnao rqjp r   rjqp ')

def obtain_suitable_comment_test():
    text = (
        "Test --- fnwo\n"
        "--- abc\n"
        "--\n"
        "-\n")
    reg='---.*'
    print(obtain_suitable_comment(text, reg))
    assert(obtain_suitable_comment(text, reg) == (
        "Test  \n"
        " \n"
        "--\n"
        "-\n"
        ))
