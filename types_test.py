import os

##Песочница - упражнения по типам и их стандартным методам
os.path.isfile()
print("Below you can see path to current dir")
print(os.path.abspath(os.path.curdir))
#
#lists Список
vegetables = ["potato", "potato", "broccoli", "garlic"]

# print(vegetables)

vegetables.sort()
print(vegetables)

vegetables.pop()
print(vegetables)

# print(vegetables.count("potato"))

numbers = {1, 2, 3, 4 }
print(numbers)

mosk={"Oy": "We", "Wey": "Me"}

bio_dict={"name": "Kosta", "age": 40, "location": "Tbilisi", "hobby": ["sleep", "walk", "guitar", "eat"], "some": mosk}

print(bio_dict)