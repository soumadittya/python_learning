# looping in dictioanry

dict1 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}

# printing all the items
for i in dict1.items():
    print(i)
print("/n/n")



# printing keys and values seperately
dict2 = {"id" : "1", "name" : "soumadittya", "age" : 23, "address" : "kolkata"}
for x, y in dict2.items():
    print("key : ", x, "    value : ", y)
