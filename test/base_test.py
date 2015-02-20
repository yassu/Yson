from sys import path
path.append('src')
from base import obtain_suitable_comment


def obtain_suitable_comment_test():
    text = (
        "Test --- fnwo\n"
        "--- abc\n"
        "--\n"
        "-\n")
    reg = '---.*'
    assert(obtain_suitable_comment(text, reg) == (
        "Test  \n"
        " \n"
        "--\n"
        "-\n"
    ))
