# tuple is a collection which is ordered and unchangeable
# ordered - means the order of elements cannot be changed after the tuple has been created
# unchangeable - meaning that we cannot change, add or remove items after the tuple has been created
# tuples are written with round brackets
# allows duplicate unlike set


# ******** if you want to add new item to tuple then rather than adding
# ******** a particular element to the tuple add a new tuple to the existing tuple

# declaring a tuple
# using the tuple constructor
t1 = tuple()

# method - 1 : initializing a tuple directly
t2 = ("apple", "banana", "cherry", "apple", "cherry")
print("t2 : ", t2)

# method - 2 : initializing a tuple using a tuple constructor
t2 = tuple((2, 4, 6))
print("t2 initialized using tuple() constructor : ", t2)

# length of a tuple
t3 = ("apple", "banana", "cherry", "apple", "cherry")
print("Length of t3 : ", len(t3))

# a single tuple can have different datatypes
t4 = ("apple", 10, "guava", 5.9)
print("t4 : ", t4)