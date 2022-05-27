#!/usr/bin/env python3

import random
from time import time


def sort_012(input_list: list) -> list:
    """Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list (list): List to be sorted

    Returns:
        list: The sorted version of the input list

    Raises:
        AttributeError: If the argument is not a list or an empty list
    """

    # Check arguments
    if not isinstance(input_list, list):
        raise AttributeError("The input list must be an actual list.")
    if len(input_list) == 0:
        raise AttributeError("The input list can't be empty.")

    i = 0
    left = 0
    right = len(input_list) - 1

    while i <= right:
        v = input_list[i]
        if v == 0:
            input_list[i] = input_list[left]
            input_list[left] = v
            left += 1
            i = max(i, left)
        elif v == 2:
            input_list[i] = input_list[right]
            input_list[right] = v
            right -= 1
        else:
            i += 1

    return input_list


def test_function(test_case):
    actual = sort_012(test_case)
    expected = sorted(test_case)
    if expected == actual:
        print("Pass")
    else:
        print(f"Fail; expected = {expected}, actual = {actual}")


def given_tests():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# noinspection PyBroadException
def user_tests():
    """Runs the user tests."""

    # Set some testing constants
    n_errors = 0

    # Test set 1 - Invalid arguments
    print("\nUser test set 1 - Invalid arguments.")
    test = 0
    for array in [3.5, "4", [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            sort_012(input_list=array)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    # Test set 2 - Test the sort function
    print("\nUser test set 2 - Testing the sort function.")
    test = 0
    for array in [[0], [1, 1], [2, 1], [2, 2, 2], [0, 0, 0]]:
        test += 1
        sort_012(input_list=array)
        expected = sorted(array)
        if array == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {array}.")
            n_errors += 1

    # User Test Case 3 - Scaling test of sort
    print("\nUser test set 3 - sort O(n) runtime complexity check.")
    times = []
    e_values = [5 + i for i in range(3)]
    test = 0
    for e in e_values:
        test += 1
        array = [random.randint(0, 2) for _ in range(10 ** e)]
        start_time = time()
        sort_012(input_list=array)
        times.append(time() - start_time)
        print(f"\tTest {test} completed in {times[-1]:.2f} seconds for n = 10^{e}.")
        del array

    print("\tSize, time (s),    n,  actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},    {times[i]:.3f}, {n:>4}, {times[i]/times[0]:>6.1f}")
    print("You can see the scaled time is rising slightly below n.")
    print("This agrees with a time complexity of O(n).")
    print("Note we are using a random set of values so the run time is less than the worse case.")

    print("\n*******************")
    if n_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")


# **********************************************************
if __name__ == '__main__':
    given_tests()
    user_tests()
