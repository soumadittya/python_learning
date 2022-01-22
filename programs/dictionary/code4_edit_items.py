# edit items

dict1 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}

# changing age
dict1["age"] = 33

# changing address
dict1["address"] = "west bengal"

print("dict1 final : ", dict1)

# using the update() method
dict2 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
dict2.update({"age" : 43, "address" : "delhi"})
print("dict2 final : ", dict2)

# update() function can also be used for adding new items to a dictionary
dict3 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
dict3.update({"gender" : "male"})
print("dict1 final : ", dict3)
