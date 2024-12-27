# name = input("What's your name?: ")
# if name == 'Megha':
#     print("Hello, nice to see you {}".format(name))
# elif name == 'Manoj':
#     print("Hello, you are a great person")
# elif name != 'Nikky':
#     print("You are not Nikky")
# elif name == 'Vikky':
#     print("Hi, {}, let's have lunch soon".format(name))
# else:
#     print('Have a nice Day!')


# Calculator

on = True

def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a+b)

def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a-b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a*b)

def devide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a/b)
while on:
    operator = input("Please type +, -, *, /, or q ")
    if operator == '+':
        add()
    elif operator == '-':
        subtraction()
    elif operator == '*':
        multiply()
    elif operator == '/':
        devide()
    elif operator == 'q':
        on = False
    else:
        print("Operation is not avilable")