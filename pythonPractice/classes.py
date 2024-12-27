'''
__init__
    sets attributes for an object at object creation, is a constructor

    __init__ method is not required but is generally used to set default state of object when it is created.

    The __init__ method is the first method for a class

    The word constructor is another word that can be used to refer to the __init__ method.
'''
from random import random


class Person:
    def __init__ (self, firstname, lastname,health, status):
        "Initialize attributes to be used in/available for all class methods in this class, and for class objects created by this class."
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname,self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion ==1:
            print("{} is happy today".format(self.firstname))
        elif emotion ==2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is bit tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >=40:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconcious.".format(self.firstname))



Manoj = Person("Manoj","Megha",85,True)
Megha = Person('Megha', 'Manoj', 98, True)

print("{} is my friend? {}".format(Manoj.firstname,Manoj.status))
print("{}'s current healthy status is at {}%. ".format(Megha.firstname, Megha.health))


Manoj.introduce()
Megha.introduce()

Manoj.status_change()