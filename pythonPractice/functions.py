# def addition(a,b):
#     return (a+b)
#
# a = 13
# b = 16
# print(addition(a,b))

#
# def addition():
#     a = int(input("Enter your first number: "))
#     b = int(input("Enter your second number: "))
#     print(a+b)
#
# addition()
#Positional Arguments
# def user_info (name, age, city):
#     print("{} is {} years old, from {}".format(name,age,city))
#
# user_info("manoj", 29, "Watford")

#Keyword arguments
# def user_info (name, age =18, city= "Hyderabad"):
#      print("{} is {} years old, from {}".format(name,age,city))
#
# user_info(name="Manoj",city= "London")

# ### *args | allows for unlimited variables to be passed into a function without defining them ahead of time
# def add(*args):
#     print(sum(args))
# add(2,3,4,5,184)

### **kwargs | allows for unlimited keyword arguments to be passed into a function without defining them ahead of time
# def application(**kwargs):
#     print(kwargs)
# application(name = "Manoj", email = "test@manoj.com")
#
# def application(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# application(name="Manoj", email="test@manoj.com")

###Combining arg types
## All three argument types can be used in a single function. They must be used in order : formal positional arguments, *args, **kwargs.
def application(fname,lname,email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname,lname,company,email))

application("manoj","m","test@gmail.com","company",75000, start_date = "21-01-24")
