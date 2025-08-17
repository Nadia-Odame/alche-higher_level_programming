#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
