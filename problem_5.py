#!/usr/bin/env python3
import random
from time import time


class TrieNode:
    """This a copy from the Udacity Workbook also copied to in this repo as 'Trie.ipynb'."""
    def __init__(self, character=None):
        self.character = character
        self.word_end = False
        self.children = {}
        self.suffix_list = []

    def insert(self, character):
        if character not in self.children.keys():
            self.children[character] = TrieNode(character)

    def collect_suffixes(self, suffix, node):
        for character, node in node.children.items():
            if node.word_end:
                self.suffix_list.append(suffix + character)
            self.collect_suffixes(suffix + character, node)

    def suffixes(self):
        self.collect_suffixes('', self)
        return self.suffix_list


class Trie:
    """Copied from Udacity problem 5 workbook."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts the given word into the trie.

        Args:
            word (str): The word string to insert.

        Raises:
            AttributeError: If the argument is not a string
        """

        # Check arguments
        if not isinstance(word, str):
            raise AttributeError("The word must be a string.")

        if len(word) > 0:
            node = self.root
            for character in word:
                node.insert(character)
                node = node.children[character]
            node.word_end = True

    def find(self, prefix: str) -> TrieNode | None:
        """Returns the node at the end of the given prefix or None is not found.

        Args:
            prefix (str): The Prefix to search for

        Returns:
            TrieNode | None: The desired node or None if not found

        Raises:
            AttributeError: If the argument is not a string
        """

        # Check arguments
        if not isinstance(prefix, str):
            raise AttributeError("The prefix must be a string.")

        # Check for empty prefixes
        if len(prefix) == 0:
            return None

        node = self.root
        for character in prefix:
            if character not in node.children.keys():
                return None
            node = node.children[character]
        return node


def given_tests() -> int:
    print("\nThe given tests were in a Jupyter Notebook Widget that can't be executed in this environment.")
    return 0


def test_invalid_insert_arguments() -> int:
    """Test the insert method with invalid arguments.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    good_trie = Trie()
    for arg in [3.5, 2, [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            good_trie.insert(word=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    return n_errors


def test_invalid_find_arguments() -> int:
    """Test the find method with invalid arguments.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    good_trie = Trie()
    for arg in [3.5, 2, [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            good_trie.find(prefix=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    return n_errors


def test_find() -> int:
    """Test the find method.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0

    # Create a Trie of 10 random lower case words of length 1 through 5
    suffixes = ["".join([chr(random.randint(97, 122)) for _ in range(random.randint(1, 5))]) for __ in range(10)]
    words = ["".join(suffixes[:i]) for i in range(1, len(suffixes)+1)]

    trie = Trie()
    for word in words:
        trie.insert(word=word)

    # Check that only strings representing words are found
    full_string = words[-1] + "extra"
    for sub_string in [full_string[:i] for i in range(len(full_string))]:
        test += 1
        actual = trie.find(prefix=sub_string)

        if (len(sub_string) == 0) or (not words[-1].startswith(sub_string)):
            if actual is None:
                print(f"Test {test} passed.")
            else:
                print(f"Test {test} failed: sub_string = {sub_string}, actual is a Node but expected None.")
                n_errors += 1
        else:
            if actual is None:
                print(f"Test {test} failed: sub_string = {sub_string}, actual is a None but expected a Node.")
                n_errors += 1
            elif sub_string in words and not actual.word_end:
                print(f"Test {test} failed: sub_string = {sub_string} is in words but the word end is False.")
                n_errors += 1
            elif sub_string not in words and actual.word_end:
                print(f"Test {test} failed: sub_string = {sub_string} is not in words but the word end is True.")
                n_errors += 1
            else:
                print(f"Test {test} passed.")

    return n_errors


def test_scale() -> int:
    """Test the time complexity.

    Returns:
        int: The number of errors
    """

    insert_times = []
    find_times = []
    e_values = [5 + i for i in range(3)]
    test = 0
    for e in e_values:
        trie = Trie()
        word = "".join([chr(random.randint(97, 122)) for _ in range(10**e)])

        test += 1
        start_time = time()
        trie.insert(word=word)
        insert_times.append(time() - start_time)
        print(f"\tTest {test} insert completed in {insert_times[-1]:.2f} seconds for n = 10^{e}.")

        test += 1
        start_time = time()
        trie.find(prefix=word)
        find_times.append(time() - start_time)
        print(f"\tTest {test} find completed in {find_times[-1]:.2f} seconds for n = 10^{e}.")

    print("")
    print("\t     |  time in sec  |   |  Scaled time")
    print("\tSize | insert | find | n | insert | find")
    print("\t-----------------------------------------")
    n_errors = 0
    for i in range(len(e_values)):
        n = 10 ** (e_values[i] - e_values[0])
        s_insert = insert_times[i]/insert_times[0]
        s_find = find_times[i]/find_times[0]
        line = f"\t10^{e_values[i]} | {insert_times[i]:>6.3f} | {find_times[i]:.3f} | {n:>4} | "
        line += f"{s_insert:>6.1f} | {s_find:>6.1f}"
        print(line)
        if (s_insert/n > 2) or (s_insert/n < 0.5) or (s_find/n > 2) or (s_find/n < 0.5):
            print(f"Time complexity check for n = {n} failed.")
            n_errors += 1

    print("You can see the scaled time is rising slightly above n.")
    print("This agrees with a time complexity of O(n).")

    return n_errors


# noinspection PyBroadException
def user_tests() -> int:
    """Runs the user tests.

    Returns:
        int: The number of errors detected.
    """

    n_errors = 0

    # Test set 1 - Invalid arguments
    print("\nUser test set 1 - Invalid insert arguments.")
    n_errors += test_invalid_insert_arguments()

    # Test set 2 - Invalid find arguments
    print("\nUser test set 2 - Invalid find arguments.")
    n_errors += test_invalid_find_arguments()

    # Test set 3 - Test find capability
    print("\nUser test set 3 - Test find capability.")
    n_errors += test_find()

    # Test set 4 - Time complexity check
    print("\nUser test set 4 - O(n) runtime complexity check.")
    n_errors += test_scale()

    return n_errors


# **********************************************************
if __name__ == '__main__':
    n_total_errors = 0
    n_total_errors += given_tests()
    n_total_errors += user_tests()

    print("\n*******************")
    if n_total_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_total_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")
