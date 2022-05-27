#!/usr/bin/env python3

from math import log2
import random
from time import time


def get_min_max(array: list) -> tuple:
    """Returns a tuple(min, max) out of list of unsorted integers in O(n) time without built-in functions.

    Bonus Challenge: Is it possible to find the max and min in a single traversal?

    Args:
       array (list of int): List containing one or more integers

    Returns:
        int: The minimum value from the given list
        int: The maximum value from the given list

    Raises:
        AttributeError: If the argument is not a list or an empty list
    """

    # Check arguments
    if not isinstance(array, list):
        raise AttributeError("The input list must be an actual list.")
    if len(array) == 0:
        raise AttributeError("The input list can't be empty.")

    max_value = min_value = array[0]
    for v in array:
        if v < min_value:
            min_value = v
        elif v > max_value:
            max_value = v

    return min_value, max_value


def given_tests():
    array = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(array)

    print("Pass" if ((0, 9) == get_min_max(array)) else "Fail")


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
            get_min_max(array=array)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    # Test set 2 - Test the function
    print("\nUser test set 2 - Testing the min-max function.")
    test = 0
    for array in [[0], [1, 1], [2, 1], [2, 2, 2], [0, 0, 0], [-1], [-1, -3, 0]]:
        test += 1
        actual = get_min_max(array=array)
        expected = (min(array), max(array))
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {actual}.")
            n_errors += 1

    # User Test Case 3 - Scaling test
    print("\nUser test set 3 - O(n) runtime complexity check.")
    times = []
    e_values = [5 + i for i in range(3)]
    test = 0
    for e in e_values:
        test += 1
        array = [random.randint(-100, 100) for _ in range(10 ** e)]
        start_time = time()
        get_min_max(array=array)
        times.append(time() - start_time)
        print(f"\tTest {test} completed in {times[-1]:.2f} seconds for n = 10^{e}.")
        del array

    print("\tSize, time (s),    n, log n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},    {times[i]:.3f}, {n:>4},  {log2(n):>4.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the scaled time is rising slightly below n but greater than log n.")
    print("This agrees with a time complexity of O(n).")

    print("\n*******************")
    if n_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")


# **********************************************************
if __name__ == '__main__':
    given_tests()
    user_tests()
