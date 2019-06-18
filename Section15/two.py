#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 102
Creating Objects
'''

import one
print("TOP LEVEL ONE.PY")
one.func()

if __name__ == '__main__':
    print("two.py has been run directly")
else:
    print("two.py has been imported")
