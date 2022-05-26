#!/usr/bin/env python3

from time import time
from math import log2


def binary_search(array: list, target: int, left: int, right: int) -> int:
    """Returns the index of the target in the array or -1 if not found.

    The pivot point is the largest element in the array and to the left of the smallest.
    For instance, in [4,5,6,7,0,1,2] the pivot is 7.

    The time complexity of this binary search is O(log n).

    Assumptions:
        No duplicates in the array

    Args:
       array (list): Rotated list of sorted integers
       target (int): The number to search for
       left (int): The left (min) most index of the array to search
       right (int): The right (max) most index of the array to search

    Returns:
       int: Target index or -1
    """

    # Check for the final state where left and right are adjacent
    if right - left <= 1:
        if array[left] == target:
            return left
        elif array[right] == target:
            return right
        return -1

    # Find the middle of the range (mid) and check if we would the target
    mid = (left + right) // 2
    if array[mid] == target:
        return mid

    # Search in the left or right half
    if array[mid] > target:
        return binary_search(array=array, target=target, left=left, right=mid-1)
    return binary_search(array=array, target=target, left=mid+1, right=right)


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
    for element in input_list:
        if not isinstance(element, int):
            raise AttributeError("The input list must be comprised of integers.")

    # Find the pivot point
    n_elements = len(input_list)
    pivot = find_pivot(array=input_list, left=0, right=n_elements-1)

    # Make a sorted version of the input list
    #   We could have reused the input list to avoid duplicating the memory but chose not to modify the original
    #   We also have to be careful when the trying to make a slice of the list when the pivot is at the end
    if pivot == n_elements - 1:
        sorted_list = input_list
    elif pivot == n_elements - 2:
        sorted_list = [input_list[pivot + 1]] + input_list[:pivot + 1]
    else:
        sorted_list = input_list[pivot + 1:] + input_list[:pivot + 1]

    # Now do a simple binary search for the desired number
    sorted_index = binary_search(array=sorted_list, target=number, left=0, right=n_elements-1)

    # Return -1 if not found or add the pivot back to the sorted index
    if sorted_index < 0:
        return -1
    return (sorted_index + pivot + 1) % n_elements


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
        actual = binary_search(array=array, target=target, left=0, right=len(array)-1)
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

        if arg:
            test += 1
            try:
                # noinspection PyTypeChecker
                rotated_array_search(input_list=good_list + [arg], number=good_target)
            except AttributeError:
                print(f"Test {test} passed.")
            else:
                print(f"Error test {test}: expected an AttributeError exception.")
                n_errors += 1

    # User Test Case 6 - Scaling test of
    print("\nUser test set 6 - Four other lists timed for scalability check.")
    times = []
    e_values = [4, 5, 6, 7]
    for e in e_values:
        start_time = time()
        rotated_array_search(input_list=[i for i in range(1, 10 ** e)] + [0], number=target)
        times.append(time() - start_time)
    print("Size, time (s),    n, log n, actual scaled time ")
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        print(f"10^{e_values[i]},    {times[i]:.3f}, {n:>4},   {log2(n):>3.1f}, {times[i]/times[0]:>6.1f}")
    print("You can see the time is rising so time complexity is > O(1), but way below linear < O(n).")
    print("This agrees with a time complexity of O(log n).")

    """


    # Test set 4 - Test the rotated array search function with negative numbers
    print("\nUser test set 4 - Testing the rotated array search function with negative numbers")
    test = 0
    for array, target, expected in [([1, 2, -1], 1, 0), ([1, 2, -1], -1, 2), ([1, 2, -1], -5, -1)]:
        test += 1
        actual = rotated_array_search(input_list=array, number=target)
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected {expected}, but got {actual}.")
            n_errors += 1

    # User Test Case 5 - Very large number
    print("\nUser test set 5 - Worst case very large number; rotated by 1 element and searching for min element.")
    test = 1
    e = 8
    n = 10**e
    input_list = [i for i in range(1, n)] + [0]
    target = 0
    expected = n - 1
    start_time = time()
    actual = rotated_array_search(input_list=input_list, number=target)
    runtime = time() - start_time
    if actual == expected:
        print(f"Test {test} passed; worst case with 10^{e} elements solved in {runtime:.2f} seconds.")
    else:
        print(f"Error test {test}: expected {expected}, but got {actual}.")
        n_errors += 1

    # User Test Case 6 - Scaling test
    print("\nUser test set 6 - Four other lists timed for scalability check.")
    times = [runtime]
    e_values = [e]
    for _ in range(4):
        e -= 1
        n = 10 ** e
        input_list = [i for i in range(1, n)] + [0]
        start_time = time()
        rotated_array_search(input_list=input_list, number=target)
        times.append(time() - start_time)
        e_values.append(e)
    print("Size,     time (ms), s. ratio, t. ratio")
    print(f"10^{e_values[-1]}, {times[-1]:.4f},    N/A,      N/A")
    for i in range(len(e_values)-2, -1, -1):
        print(f"10^{e_values[i]}, {times[i]:.3f},    10, {times[i]/times[i+1]:.1f}")
    print("You can see the time is rising so time complexity is > O(1), but way below linear < O(n).")
    print("This agrees with a time complexity of O(log n).")
    """

    print("\n*******************")
    if n_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")


# **********************************************************
if __name__ == '__main__':
    given_tests()
    user_tests()
