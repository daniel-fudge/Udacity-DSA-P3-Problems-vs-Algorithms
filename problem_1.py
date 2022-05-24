#!/usr/bin/env python3

from time import time


def modified_binary_search(squared_value: int, left: int, right: int, debug: bool = False) -> int:
    """A modified binary search that looks for the square root of the given value.

    Args:
        squared_value (int): The integer that we wish to find the square root of.
        left (int) : The lowest value in the range of possible values.
        right (int): The highest value in the range of possible values.
        debug (bool): Print extra info if True

    Returns:
        int: The floored integer square root of the given value.
    """

    # If left and right next to each other, the square root must be a float between them
    if right - left <= 1:
        if debug:
            print(f"left={left}, right={right}")
        return left

    center = (left + right) // 2
    center_squared = center ** 2

    # If the squared values match, we have found the square root
    if center_squared == squared_value:
        if debug:
            print(f"Found; center={center}, left={left}, right={right}")
        return center

    # if not, recurse either above of below the center
    if center_squared < squared_value:
        if debug:
            print(f"Recurse top; center={center}, left={left}, right={right}")
        return modified_binary_search(squared_value, center, right)
    else:
        if debug:
            print(f"Recurse bottom; center={center}, left={left}, right={right}")
        return modified_binary_search(squared_value, left, center)


def sqrt(number: int) -> int:
    """Calculate the floored square root of a number.

    Args:
       number(int): Number to find the floored squared root

    Returns:
       int: Floored Square Root

        Raises:
            AttributeError: If the given number is not a positive integer.
    """

    # Check arguments
    if not isinstance(number, int):
        raise AttributeError("The number must be an integer.")
    if number < 0:
        raise AttributeError("The number must be a positive integer.")

    # 0 and 1 are squares of themselves
    if number <= 1:
        return number

    # The square root must be between 1 and half of the number since 0 and 1 are handled above
    return modified_binary_search(number, 1, number // 2)


def given_tests():
    """Given tests."""
    print("Given tests.")
    for expected, arg in [(3, 9), (0, 0), (4, 16), (1, 1), (5, 27)]:
        print("Pass" if (expected == sqrt(arg)) else f"Fail; arg {arg}, expected {expected}, got {sqrt(arg)}")


# noinspection PyBroadException
def user_tests():
    """Runs the user tests."""

    # Set some testing constants
    n_errors = 0

    # User Test Case 1 - Error handling
    print("\nUser test set 1 - Error handling")
    test = 0
    for arg in [-1, 3.5, "4", [], None]:
        test += 1
        try:
            sqrt(arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    # User Test Case 2 - Very large number
    print("\nUser test set 2 - Very large number; (10^150)^2+1 executed 1000 times.")
    test = 1
    n = 150
    expected = 10**n
    squared_value = expected ** 2 + 1
    actual = 0
    start_time = time()
    for _ in range(1000):
        actual = sqrt(squared_value)
    runtime = time() - start_time
    if actual == expected:
        print(f"Test {test} passed; square value 10^{n}^2+1 solved 1000 times in {runtime:.4f} seconds.")
    else:
        print(f"Error test {test}: expected {expected}, but got {actual}.")
        n_errors += 1

    # User Test Case 3 - Scaling test
    print("\nUser test set 3 - Four other numbers timed for scalability check.")
    times = [runtime]
    values = [squared_value]
    for _ in range(4):
        squared_value = squared_value // (10**50)
        start_time = time()
        for _ in range(1000):
            sqrt(squared_value)
        times.append(time() - start_time)
        values.append(squared_value)
    print("value,     time (ms), v. ratio, t. ratio")
    print(f"{values[-1]:.2e}, {times[-1]:.4f},    N/A,      N/A")
    for i in range(len(values)-2, -1, -1):
        print(f"{values[i]:.2e}, {times[i]:.4f},    {values[i]/values[i+1]:.2e}, {times[i]/times[i+1]:.4f}")
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
