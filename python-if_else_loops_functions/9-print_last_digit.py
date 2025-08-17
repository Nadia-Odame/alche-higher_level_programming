#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for char in str:
        # Convert lowercase letters to uppercase using ASCII
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
