# remove items from the dictionary

# pop() function
# removes the mentioned
dict1 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
# removing 'address' field
dict1.pop("age")
print("dict1 final : ", dict1)

# popintem() function
# removes the last item
dict2 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
# removing 'address' field
dict2.popitem()
print("dict2 final : ", dict2)

# using del keyword - 1
# the following syntax will delete a particular object from the dictionary
dict3 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
del dict3["age"]
print("dict3 final : ", dict3)

# using del keyword - 2
# the following print statement will throw an error as the dict4 has been deleted
dict4 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
del dict4
# print("dict4 final : ", dict4)

# clear() function
# this will empty the whole dictionary
dict5 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
dict5.clear()
print("dict5 final : ", dict5)


