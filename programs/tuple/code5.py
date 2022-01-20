# in general adding an element to the tuple is not allowed
# but we can merge two tuples together to make it one single tuple

t1 = (0, 1, 2, 3)
t2 = (4, 5, 6, 7)

t1 = t1 + t2
print("t1 after merge: ", t1)

# suppose if we want to add a single element to a tuple
# then it is directly not possible but we can make another
# single element tuple and merge it with the main tuple
# it will look like we have added a single element to the tuple


t3 = ("apple", "banana", "mango")
t4 = ("papaya",)
# an extra comma has been added to make it a tuple otherwise
# it would be a string

t3 = t3 + t4
print(t3)
