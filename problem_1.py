#!/usr/bin/env python3

from time import time



def given_tests():

    test = 0


# noinspection PyBroadException
def user_tests():
    """Runs the user tests."""

    # Set some testing constants
    n_errors = 0


    print("\n*******************")
    if n_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")


# **********************************************************
if __name__ == '__main__':
    given_tests()
    user_tests()
