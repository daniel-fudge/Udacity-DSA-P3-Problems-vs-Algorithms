#!/usr/bin/env python3


class RouteTrieNode:
    """A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler."""

    def __init__(self, path: str):
        self.path = path
        self.handler = None
        self.children = {}

    def insert(self, path: str):
        if path not in self.children.keys():
            self.children[path] = RouteTrieNode(path)


class RouteTrie:
    """A RouteTrie will store our routes and their associated handlers"""

    def __init__(self, root_handler: str):
        self.root = RouteTrieNode(path="")
        self.root.handler = root_handler

    def insert(self, full_path: str, handler: str):
        """Inserts the given full path into the Route Trie.

        Args:
            full_path (str): The full path to insert.
            handler (str): The handler to add to the leaf node.

        Raises:
            AttributeError: If the given path has no non-slash characters.
        """

        # Remove leading and trailing  "/" from the given path
        full_path = full_path.strip("/")

        # Check for an empty full path
        if len(full_path) == 0:
            raise AttributeError("Given path has no non-slash characters.")

        # Loop over all the paths between the "/" characters
        node = self.root
        for path in full_path.split('/'):
            node.insert(path=path)
            node = node.children[path]
        node.handler = handler

    def find(self, full_path: str):
        """Starting at the root, find match for given full path and return the matching handler or None for no match.

        Args:
            full_path (str): The full path we need to match.

        Returns:
            str | None: The handle of the matching path or None if not found
        """

        # Remove leading and trailing  "/" from the given path
        full_path = full_path.strip("/")

        # Check for an empty full path, which matches the root
        if len(full_path) == 0:
            return self.root.handler

        node = self.root
        for path in full_path.split('/'):
            if path not in node.children.keys():
                return None
            node = node.children[path]
        return node.handler


class Router:
    """The HTTP Router class."""
    def __init__(self, root_handler: str, error_handler: str):
        """The object instantiation method.

        Args:
            root_handler (str): The handler for the root of the object.
            error_handler (str): The handler returned when a route is not found (404 error).

        Raises:
            AttributeError: If either argument is not a string
        """

        # Check arguments
        if not isinstance(root_handler, str):
            raise AttributeError("The root_handler must be a string.")
        if not isinstance(error_handler, str):
            raise AttributeError("The error_handler must be a string.")

        self.trie = RouteTrie(root_handler=root_handler)
        self.error_handler = error_handler

    def add_handler(self, full_path: str, handler: str):
        """Adds the given handler to the node at the end of the full path.

        Args:
            full_path (str): The full path to insert.
            handler (str): The handler to add to the leaf node.

        Raises:
            AttributeError: If either argument is not a string
            AttributeError: If the given path has no non-slash characters.
        """
        # Check arguments
        if not isinstance(full_path, str):
            raise AttributeError("The full_path must be a string.")
        if not isinstance(handler, str):
            raise AttributeError("The handler must be a string.")
        if len(full_path.replace("/", "")) == 0:
            raise AttributeError("The full_path has no non-slash characters.")

        self.trie.insert(full_path=full_path, handler=handler)

    def lookup(self, full_path: str):
        """Return handler for given full path or the error handler for no match.

        Args:
            full_path (str): The full path we need to match.

        Returns:
            str | None: The handle of the matching path or None if not found

        Raises:
            AttributeError: If argument is not a string
        """

        # Check arguments
        if not isinstance(full_path, str):
            raise AttributeError("The full_path must be a string.")

        handler = self.trie.find(full_path=full_path)
        if handler is None:
            return self.error_handler
        return handler


def given_tests() -> int:
    """Runs the tests defined by Udacity.

    Returns:
        int: The number of failed tests.
    """

    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print("\nGiven tests:")
    test = 0
    n_errors = 0
    for path, expected in [("/", 'root handler'), ("/home", 'not found handler'), ("/home/about", 'about handler'),
                           ("/home/about/", 'about handler'), ("/home/about/me", 'not found handler')]:
        actual = router.lookup(full_path=path)
        test += 1
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Test {test} failed: path = {path}, actual = {actual}, expected = {expected}.")
            n_errors += 1
    """
    These are actual tests in Udacity before reformatting
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
    """

    return n_errors


def test_handler_not_found() -> int:
    """Test the handler not found capability.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    good_handler = "good_handler"
    error_handler = "error_handler"
    good_router = Router(root_handler=good_handler, error_handler=error_handler)

    # Create a path with handle on every second sub path
    full_path = ""
    n_paths = 5
    for p in range(n_paths):
        full_path += f"/path{p}"
        if p % 2 == 0:
            good_router.add_handler(full_path=full_path, handler=good_handler)

    # Check that only every second path has a handle
    full_path = ""
    for p in range(n_paths):
        test += 1
        full_path += f"/path{p}"
        actual = good_router.lookup(full_path=full_path)
        if p % 2 == 0:
            expected = good_handler
        else:
            expected = error_handler

        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Test {test} failed: path = {full_path}, actual handler = {actual}, expected = {expected}.")
            n_errors += 1

    return n_errors


def test_invalid_arguments() -> int:
    """Test the top level methods with invalid arguments.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    bad_path = "///"
    good_handler = "good_handler"
    good_path = "/some/good/path"
    good_router = Router(root_handler=good_handler, error_handler=good_handler)
    for arg in [3.5, 2, [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            Router(root_handler=arg, error_handler=good_handler)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

        test += 1
        try:
            # noinspection PyTypeChecker
            Router(root_handler=good_handler, error_handler=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

        test += 1
        try:
            # noinspection PyTypeChecker
            good_router.add_handler(full_path=arg, handler=good_handler)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

        test += 1
        try:
            # noinspection PyTypeChecker
            good_router.add_handler(full_path=good_path, handler=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

        test += 1
        try:
            # noinspection PyTypeChecker
            good_router.lookup(full_path=arg)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    test += 1
    try:
        # noinspection PyTypeChecker
        good_router.add_handler(full_path=bad_path, handler=good_handler)
    except AttributeError:
        print(f"Test {test} passed.")
    else:
        print(f"Error test {test}: expected an AttributeError exception.")
        n_errors += 1

    return n_errors


def test_slashes() -> int:
    """Test multiple leading and trailing edge slashes.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    good_handler = "good_handler"
    good_router = Router(root_handler=good_handler, error_handler=good_handler)
    for path in [f"{'/'*i}some/middle/content{'/'*j}" for i in range(3) for j in range(3)]:
        test += 1
        good_router.add_handler(full_path=path, handler=good_handler)
        handler = good_router.lookup(full_path=path)
        if handler == good_handler:
            print(f"Test {test} passed.")
        else:
            print(f"Test {test} failed: path = {path}, actual handler = {handler}, expected = {good_handler}.")
            n_errors += 1

    return n_errors


# noinspection PyBroadException
def user_tests() -> int:
    """Runs the user tests."""

    n_errors = 0

    # Test set 1 - Invalid arguments
    print("\nUser test set 1 - Invalid arguments.")
    n_errors += test_invalid_arguments()

    # Test "not found handler" (BONUS POINTS)
    print("\nUser test set 2 - 'Not found handler' (BONUS POINTS).")
    n_errors += test_handler_not_found()

    # Test multiple leading and trailing "/" (MORE BONUS POINTS)
    print("\nUser test set 3 - Leading and training '/' (MORE BONUS POINTS).")
    n_errors += test_slashes()

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
