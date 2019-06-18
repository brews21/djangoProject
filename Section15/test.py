#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Django course
Learning Python 102
Creating Objects
'''

class Dog():
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius**2 * self.pi

    def set_radius(self, new_r):
        self.radius = new_r

mydog = Dog("Lab", "mike")
#print(mydog.species)


mycircle = Circle(3)
print(mycircle.area())
mycircle.set_radius(2)
print(mycircle.area())


#Error handling

try:
    f = open("notes.txt", "w")
    f.write("Hello World")
except:
    print("ERROR")
finally:
    print("finally")
    f.close()


# Regular Expressions
import re

def mulit_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This iS a strIng! But is has #puNctuAtion. How cAn we rEMove it -- 123w2423'

test_patterns = ['[^!.?#]+']
mulit_re_find(test_patterns,test_phrase)
test_patterns = ['[a-z]+']
mulit_re_find(test_patterns,test_phrase)
test_patterns = ['[A-Z]+']
mulit_re_find(test_patterns,test_phrase)
test_patterns = [r'\d+']
mulit_re_find(test_patterns,test_phrase)
test_patterns = [r'\W+']
mulit_re_find(test_patterns,test_phrase)
