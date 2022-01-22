# copy function

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

# copy function()
# it will make a copy of a dictionary to another variable
dict2 = dict1.copy()
# checking whetehr dict1 is equal to dict 2
print("Checking 1 : ", dict1 == dict2)

# changing dict_1

dict1 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  }
}

# checking again whether dict1 is equal ti dict2
print("Checking 2 : ", dict1 == dict2)

