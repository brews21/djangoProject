#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 102
Creating Objects
'''

class Animal():
    """docstring for Animal."""

    type = ""

    def __init__(self):
        self.type = "Animal"
        print("Animal Created")

    def __str__(self):
        return self.type

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")



class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.type = "Dog"
        print("DOG Created")


mydog = Dog()
mydog.whoAmI()
mydog.eat()

print(mydog)
myanimal = Animal()
print(myanimal)
