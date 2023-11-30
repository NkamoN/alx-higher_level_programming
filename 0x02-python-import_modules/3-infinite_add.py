#!/usr/bin/python3

import sys

# Function adds integers
def add_integers(*args):
    return sum(int(arg) for arg in args)

arguments = sys.argv[1:]

result = add_integers(*arguments)
print(result)
