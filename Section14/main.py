#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 101
'''

#List Comprehenstion
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)

# reverse a string
s = "django"
print(s[::-1])


def add_num(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1 + num2
    else:
        return "I need Ints"

print(add_num(1,2))
print(add_num(1,"2"))


#Lamda Expressions

mylist = [1,2,3,4,5,6]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))

print(list(filter(lambda num:num%2 == 0, mylist)))
