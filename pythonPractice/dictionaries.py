years = {"Manoj":1994,"Megha":1996}

print(years.get("Manoj"))

print(years.items())

print(years.keys())

print(years.values())

years.popitem()
print(years)

print(years.setdefault("friends",123))
print(years)

date = {'sep':11, 'may':30}
years.update(date)
print(years)

years.update(Manoj = 1995)
print(years)














