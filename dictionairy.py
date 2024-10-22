#dictionairy

data = {1: "Python",
        2: "C++",
        3: "Python",
        4: "Java",
        5: "Lua"}

print(data[2])

print(data[7]) #error - 7 is not on the data variable

#get() method

print(data.get[3])
print(data.get(4)) #output = None
print(data.get(4, "Not Found"))

keys = ["Chocolate", "Vegetables", "Fruits"] #list1
values = ["Java", "Lua", "C++"] #list2

data1 = dict(zip(keys, values))

print(data1)

del dict["Lua"]

data1 = ["C", "CC", "CCC"]

cars = {1: "BMW",
        2: "Audi",
        3: "Porsche",
        4: "Mercedes"}
print(cars)
cars.popitem()
print(cars)