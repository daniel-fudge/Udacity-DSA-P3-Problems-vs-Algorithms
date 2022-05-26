#!/usr/bin/env python3

from time import time
from math import log2


def binary_search(array: list, target: int, left_sorted: int, right_sorted: int, pivot: int) -> int:
    """Returns the index of the target in the array or -1 if not found.

    The pivot point is the largest element in the array and to the left of the smallest.
    For instance, in [4,5,6,7,0,1,2] the pivot is 7.

    The time complexity of this binary search is O(log n).

    Assumptions:
        No duplicates in the array

    Args:
       array (list): Rotated list of sorted integers
       target (int): The number to search for
       left_sorted (int): The left (min) most index of the array to search assuming the array was sorted
       right_sorted (int): The right (max) most index of the array to search assuming the array was sorted
       pivot (int): The pivot point that creates a fully sorted array

    Returns:
       int: Target index or -1
    """

    # Convert the sorted indices to unsorted
    n_elements = len(array)
    right = (right_sorted + pivot + 1) % n_elements
    left = (left_sorted + pivot + 1) % n_elements

    # Check for the final state where left and right are adjacent
    if right_sorted - left_sorted <= 1:
        if array[left] == target:
            return left
        elif array[right] == target:
            return right
        return -1

    # Find the middle of the range (mid) and check if we would the target
    mid_sorted = (left_sorted + right_sorted) // 2
    mid = (mid_sorted + pivot + 1) % n_elements
    if array[mid] == target:
        return mid

    # Search in the left or right half
    if array[mid] > target:
        return binary_search(array=array, target=target, left_sorted=left_sorted, right_sorted=mid_sorted-1,
                             pivot=pivot)
    return binary_search(array=array, target=target, left_sorted=mid_sorted+1, right_sorted=right_sorted, pivot=pivot)


def find_pivot(array: list, left: int, right: int) -> int:
    """Finds pivot point of the rotated sorted array.

    The pivot point is the largest element in the array and to the left of the smallest.
    For instance, in [4,5,6,7,0,1,2] the pivot is 7.

    The time complexity of this modified binary search is O(log n).

    Assumptions:
        No duplicates in the array

    Args:
       array (list): Rotated list of sorted integers
       left (int): The left (min) most index of the array to search
       right (int): The right (max) most index of the array to search

    Returns:
       int: Pivot index
    """

    # Check to see if array is already sorted
    if array[right] > array[left]:
        return right

    # Check for the final state where left and right are adjacent
    if right - left <= 1:
        return left

    # Find the middle of the range (mid)
    mid = (left + right) // 2

    # Search in the left or right half
    if array[mid] < array[0]:
        return find_pivot(array=array, left=left, right=mid)
    return find_pivot(array=array, left=mid, right=right)


def rotated_array_search(input_list: list, number: int) -> int:
    """Finds the index by searching in a rotated sorted array with O(log n) runtime complexity.

    Assumptions:
        No duplicates in the array
        An empty input list raises an Attribute error

    Args:
       input_list (list): Rotated list of sorted integers
       number (int): The number to search for within the input array

    Returns:
       int: Index or -1

    Raises:
        AttributeError: If the arguments are invalid
    """

    # Check arguments
    if not isinstance(number, int):
        raise AttributeError("The number must be an integer.")
    if not isinstance(input_list, list):
        raise AttributeError("The input list must be an actual list.")
    if len(input_list) == 0:
        raise AttributeError("The input list can't be empty.")

    # Find the pivot point
    n_elements = len(input_list)
    pivot = find_pivot(array=input_list, left=0, right=n_elements-1)

    # Now do a binary search for the desired number with a pivot offset to the indices
    index = binary_search(array=input_list, target=number, left_sorted=0, right_sorted=n_elements-1, pivot=pivot)

    return index


def linear_search(input_list: list, number: int) -> int:
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case: list):
    input_list = test_case[0]
    number = test_case[1]
    expected = linear_search(input_list, number)
    actual = rotated_array_search(input_list, number)
    if expected == actual:
        print("Pass")
    else:
        print(f"Fail; expected = {expected}, actual = {actual}")


def given_tests():
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# noinspection PyBroadException
def user_tests():
    """Runs the user tests."""

    # Set some testing constants
    n_errors = 0

    # Test set 1 - Test the find pivot function
    print("\nUser test set 1 - Testing the find pivot function.")
    test = 0
    for array, expected in [([4, 6, 7, 0, 1, 2], 2), ([4, 5, 6, 7, 1, 2], 3), ([4, 5, 0], 1), ([2, 5, 8], 2),
                            ([8, 1, 5], 0)]:
        test += 1
        actual = find_pivot(array=array, left=0, right=len(array)-1)
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {actual}.")
            n_errors += 1

    # Test set 2 - Test the binary search function
    print("\nUser test set 2 - Testing the binary search function.")
    test = 0
    for array, target, expected in [([1, 2, 3, 4, 6, 7, 8, 9, 10], 1, 0), ([1, 3], 1, 0), ([1, 3], 3, 1), ([3], 3, 0),
                                    ([1, 3, 7], 9, -1)]:
        test += 1
        actual = binary_search(array=array, target=target, left_sorted=0, right_sorted=len(array)-1, pivot=len(array)-1)
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {actual}.")
            n_errors += 1

    # Test set 3 - Invalid arguments
    print("\nUser test set 3 - Invalid arguments.")
    test = 0
    good_list = [1, 2, 3]
    good_target = 4
    for arg in [3.5, "4", [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            rotated_array_search(input_list=good_list, number=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

        test += 1
        try:
            # noinspection PyTypeChecker
            rotated_array_search(input_list=arg, number=good_target)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    # User Test Case 4 - Scaling test of find_pivot
    print("\nUser test set 4 - find_pivot log n runtime complexity check.")
    times = []
    e_values = [6 + i for i in range(3)]
    test = 0
    for e in e_values:
        test += 1
        array = [i for i in range(1, 10 ** e)] + [0]
        expected = 10 ** e - 2
        start_time = time()
        for _ in range(1000):
            actual = find_pivot(array=array, left=0, right=len(array) - 1)
        times.append(time() - start_time)
        if actual == expected:
            print(f"\tTest {test} passed in {times[-1]:.4f} seconds.")
        else:
            print(f"\tError test {test}: expected {expected}, but got {actual}.")
            n_errors += 1
        del array

    print("\tSize, time (ms),    n, log n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},     {times[i]:.3f}, {n:>4},  {log2(n):>4.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the time is rising so time complexity is > O(1), but way below linear < O(n).")
    print("This agrees with a time complexity of O(log n).")

    # User Test Case 5 - Scaling test of binary_search
    print("\nUser test set 5 - binary_search log n runtime complexity check.")
    times = []
    e_values = [6 + i for i in range(3)]
    test = 0
    expected = 0
    for e in e_values:
        test += 1
        array = [i for i in range(10 ** e)]
        start_time = time()
        for _ in range(1000):
            actual = binary_search(array=array, target=0, left_sorted=0, right_sorted=len(array) - 1,
                                   pivot=len(array)-1)
        times.append(time() - start_time)
        if actual == expected:
            print(f"\tTest {test} passed in {times[-1]:.4f} seconds.")
        else:
            print(f"\tError test {test}: expected {expected}, but got {actual}.")
            n_errors += 1
        del array

    print("\tSize, time (ms),    n, log n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},     {times[i]:.3f}, {n:>4},  {log2(n):>4.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the time is rising so time complexity is > O(1), but way below linear < O(n).")
    print("This agrees with a time complexity of O(log n).")

    # User Test Case 6 - Scaling test of rotated_array_search
    print("\nUser test set 6 - rotated_array_search log n runtime complexity check.")
    times = []
    e_values = [6 + i for i in range(3)]
    test = 0
    for e in e_values:
        test += 1
        array = [i for i in range(1, 10 ** e)] + [0]
        expected = 10 ** e - 1
        start_time = time()
        for _ in range(1000):
            actual = rotated_array_search(input_list=array, number=0)
        times.append(time() - start_time)
        if actual == expected:
            print(f"\tTest {test} passed in {times[-1]:.4f} seconds.")
        else:
            print(f"\tError test {test}: expected {expected}, but got {actual}.")
            n_errors += 1
        del array

    print("\tSize, time (ms),    n, log n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"\t10^{e_values[i]},     {times[i]:.3f}, {n:>4},  {log2(n):>4.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the time is rising so time complexity is > O(1), but way below linear < O(n).")
    print("This agrees with a time complexity of O(log n).")

    print("\n*******************")
    if n_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")


# **********************************************************
if __name__ == '__main__':
    given_tests()
    user_tests()
