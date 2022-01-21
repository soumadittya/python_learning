# sets are unordered, unchangeable and unindexed
# **** sets do not allow duplicate values
# **** in sets two elements cannot be same

# unordered - Unordered means that the items in a set do not have a defined order.
# unchangeable - that we cannot change the items after the set has been created

# **** You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the 'in' keyword.

# **** adding and removing items to list is allowed


# initializing a set
s1 = {"apple", "banana", "mango", "orange"}
print("printing s1 directly : ", s1)

# printing a particular element using index
# the following print statement will give an error
# s2 = {"apple", "banana", "mango", "orange"}
# print(s2[2])

# printing all elements using 'for loop' and 'in' keyboard
s3 = {"apple", "banana", "mango", "orange"}
for i in s3:
    print(i)







