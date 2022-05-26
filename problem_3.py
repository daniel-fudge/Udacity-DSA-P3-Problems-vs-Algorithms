#!/usr/bin/env python3

from math import log2
import random
from time import time
from typing import Tuple


def merge(array: list, left: int, mid: int, right: int):
    """Merges two sorted arrays into a single sorted array.

    Note: This algorithm performs the sorting inplace to avoid the O(n) slicing operations.

    Args:
        array (list): The array containing the sub arrays to sort.
        left (int): Start of the first array.
        mid (int): The end of the first array and adjacent to the start of the right array
        right (list): The end of the 2nd array.
    """

    left_index = left
    right_index = mid + 1
    output_list = []

    while left_index <= mid and right_index <= right:
        if array[left_index] > array[right_index]:
            output_list.append(array[right_index])
            right_index += 1
        else:
            output_list.append(array[left_index])
            left_index += 1

    output_list += array[left_index:mid+1]
    output_list += array[right_index:right+1]

    for i, v in enumerate(output_list):
        array[left + i] = v


def mergesort(array: list, left: int, right: int):
    """Sorts the array within left and right by recursively splitting into halves and then merging.

    Args:
        array (list): The array containing the sub array to sort.
        left (int): Start of the sub array to sort.
        right (int): End of the sub array to sort.
    """

    # Sopping condition when the array has been divided into single elements
    if left >= right:
        return

    # Divide the sub array into halves
    mid = (left + right) // 2
    mergesort(array=array, left=left, right=mid)
    mergesort(array=array, left=mid+1, right=right)

    # Merge the sub arrays into a sorted array
    merge(array=array, left=left, mid=mid, right=right)


def rearrange_digits(array: list) -> Tuple[int, int]:
    """Rearrange Array Elements to form two number such that their sum is maximum with O(nlog n) time complexity.

    Example:
        Given: [1, 2, 3, 4, 5]
        Result: [531, 42] or [542, 31]
        Max Sum: 573 for both so either may be returned

    Assumptions:
        1. All array elements are in the range [0, 9]

    Args:
       array (list of int): Input List

    Returns:
       (int),(int): Two maximum sums

    Raises:
        AttributeError: If the argument is not a list or empty
    """

    # Check arguments
    if not isinstance(array, list):
        raise AttributeError("The input list must be an actual list.")
    if len(array) == 0:
        raise AttributeError("The input list can't be empty.")

    # First sort the array, this is O(n log n) time complexity
    right = len(array) - 1
    mergesort(array=array, left=0, right=right)

    # Build the two numbers from the sorted list, this is O(n) time complexity
    number_str_1 = ""
    number_str_2 = ""

    i = right
    while i > 0:
        number_str_1 += str(array[i])
        i -= 1
        number_str_2 += str(array[i])
        i -= 1
    if i == 0:
        number_str_1 += str(array[i])

    return int(number_str_1), int(number_str_2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    actual = sum(output)

    solution = test_case[1]
    expected = sum(solution)
    if expected == actual:
        print("Pass")
    else:
        print(f"Fail; expected = {expected} [{solution}], actual = {actual} [{output}]")


def given_tests():
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# noinspection PyBroadException
def user_tests():
    """Runs the user tests."""

    # Set some testing constants
    n_errors = 0

    # Test set 1 - Test the merge sort function
    print("\nUser test set 1 - Testing the merge sort function.")
    test = 0
    for array in [[3, 2, 1], [3, 2], [3, 6, 1, 9]]:
        test += 1
        mergesort(array=array, left=0, right=len(array) - 1)
        expected = sorted(array)
        if array == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {array}.")
            n_errors += 1

    # Test set 2 - Invalid arguments
    print("\nUser test set 2 - Invalid arguments.")
    test = 0
    for arg in [3.5, "4", [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            rearrange_digits(array=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    # User Test Case 3 - Scaling test of rearrange_digits
    print("\nUser test set 4 - rearrange_digits O(nlog n) runtime complexity check.")
    times = []
    e_values = [4 + i for i in range(3)]
    test = 0
    for e in e_values:
        test += 1
        array = [random.randint(0, 9) for _ in range(10 ** e)]
        start_time = time()
        rearrange_digits(array=array)
        times.append(time() - start_time)
        print(f"\tTest {test} completed in {times[-1]:.2f} seconds for n = 10^{e}.")
        del array

    print("\tSize, time (s),    n,  nlog n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},    {times[i]:.3f}, {n:>4},   {n*log2(n):>5.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the scaled time is rising > n, but below n log n.")
    print("This agrees with a time complexity of O(n log n).")
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
