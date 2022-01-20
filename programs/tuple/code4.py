# different functions of a tuple

# checking if a particular element exists or not in tuple
t1 = ("apple", "banana", "guava", "kiwi")
if "banana" in t1:
    print("Yes....")

# changing tuple to list
t2 = ("apple", "banana", "guava", "kiwi")
# list() constructor
l1 = list(t2)
print("list - l1 : ", l1)

# converting a list to tuple
l2 = ["apple", "banana", "guava", "kiwi"]
# using tuple() constructor
t3 = tuple(l2)
print("tuple - t3 : ", t3)

# count() function
# it counts the number of times a particular value is present in the tuple
t4 = (0, 1, 4, 2, 3, 4, 6, 4, 9)
print("number of elements in 4 present in t4: ", t4.count(4))

# index() function
# it returns the index of a specific element
t5 = (0, 1, 2, 3, 4, 5, 6, 7)
print("index of 3 in t5 : ", t5.index(3))
