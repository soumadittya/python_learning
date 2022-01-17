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

