#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 102
Creating Objects
'''

def func():
    print("func() in one.py")

print("TOP LEVEL ONE.PY")

if __name__ == '__main__':
    print("one.py has been run directly")
else:
    print("one.py has been imported")
