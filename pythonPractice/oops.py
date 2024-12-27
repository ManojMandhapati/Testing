# Inheritance
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
Megha = Person('Megha', 'Manoj', 98, False)

print("{} is my friend? {}".format(Manoj.firstname,Manoj.status))
print("{}'s current healthy status is at {}%. ".format(Megha.firstname, Megha.health))



class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon


    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
             other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak.".format(other.firstname))

    def steal(self, other):
        print(" ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 'Wayne',75, False)
Alex.hurt(Manoj)
Alex.insult(Manoj)
Alex.steal(Megha)












