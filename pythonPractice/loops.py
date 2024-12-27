# For loop

# fruits = ["Apple","Grape","Banana"]
# for fruit in fruits:
#     print("Would you like {} ?".format(fruit))
#
# for num in range(1,11):
#     print("Number {} ".format(num))


############################################################################

# While loop

# temp = 40
# while temp > 32:
#     print("The water is {} degrees".format(temp))
#     temp -=1

#############################################################################

# Loop controls
 #Break - end the loop, go to the next statement in the program(outside the loop).
 #Continue - skips current part of the loop, moves to the next part of the loop.
 #Pass - skips any part of the loop where 'Pass' appears, best used for testing code.


temp = 40
while temp > 32:
    print("The water is {} degrees".format(temp))
    temp -=1
    if temp == 33:
        break

for num in range(1,11):
    if num ==7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}. ".format(num))


for num in range(1,11):
    if num ==3:
        pass
    else:
        print("This is number {}.".format(num))






