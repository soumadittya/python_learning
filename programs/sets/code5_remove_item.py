# remove item from set

# **** Difference between remove() and discard():
# If the item to be removed is not present
# remove() will raise an error
# But if item to remove is not present
# the discard will not raise an erroe

# remove() function
s1 = {"apple", "banana", "cat", "mouse"}
s1.remove("banana")
print("s1 final : ", s1)
# **** the following print statement will throw an error
# as "tiger" is not in the set


# pop() function
# deletes the last element
s2 = {"apple", "banana", "cat", "mouse"}
print("s2 pop 1 : ", s2.pop())
print("s2 pop 2 : ", s2.pop())
print("final s2 : ", s2)

# discard() function
# same as remove function
s3 = {"apple", "banana", "cat", "mouse"}
s3.remove("banana")
print("s3 final : ", s3)
# **** the following statement will not raise an error though
# "tigger" is not present in the set
s3.discard("tigger")

