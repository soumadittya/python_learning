# nested dictionary

dict1 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print("dict1 : ", dict1)

# accessing a particular item
print("dict1_child2_name : ", dict1["child2"]["name"])