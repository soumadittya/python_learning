# copying a list
# copy() function
# list() constructor

# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.

# method_1 : using copy() function
list1 = [1, 2,46, 89]
list2 = list1.copy()
print(list2)

# method_2 : using list() constructor
list3 = [3, 11, 89, 45, 46]
list4 = list(list3)
print(list4)