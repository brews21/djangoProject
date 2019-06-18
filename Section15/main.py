#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 102
Creating Objects and Functions
'''
#import module as mm
#mm.func_in_module()
from module import func_in_module
func_in_module()

def hello(name="mike"):
    print("Running hello()")
    def greet():
        print("Inside Greet()")
    def welcome():
        print("Inside welcome()")
    print("end of hello()")

    if name == "mike":
        return greet
    else:
        return welcome

x = hello()
print(x())


def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("func() has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator ")

#func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
