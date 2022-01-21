# different functions for adding elements
# append() function
# extend() function
# insert() function

# append() function
# append an element at the end of the list
list1 = ['som', 'uttam', 'sudipta']
list1.append('ghosh')
list1.append(['america', 'usa'])
print('list1 : ', list1)

# extend() function
# add the items in the list at the end of the list
list2 = ['som', 'uttam', 'sudipta']
list2.extend(['america', 'usa'])
print('list2 : ', list2)

# insert() function
# insert an element or a whole list at a particular index of the list
list3 = ['som', 'uttam', 'sudipta', 'ghosh']
list3.insert(1, 'uss')
list3.insert(3, ['america', 'usa'])
print(list3)

# adding 2 lists
list4 = ['som', 'sudipta']
list4 = list4 + ['uttam', 'uss']
print('list4 : ', list4)



