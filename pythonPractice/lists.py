fruits = ["apples",'grapes','bananas','pears',"Apples"]
seasons = ["Mansoon","Summer","Winter","Spring"]

print("Apples " in fruits)

print(fruits.count("Apples"))


print(fruits.index('Apples'))


# Append method

fruits.append("Ornages")

print(fruits, seasons)

# Extend

fruits.extend(seasons)
print(fruits)

# Remove
fruits.remove("apples")
print(fruits)

#Index
fruits.pop(0)
print(fruits)

#Sort
fruits = ["apples",'grapes','bananas','pears']

fruits.sort()

print(fruits)