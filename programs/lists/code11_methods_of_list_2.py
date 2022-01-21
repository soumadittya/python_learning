# remove item from list
# remove() function
# pop() function
# clear() function
# del keyword

# remove() function
# removes the mentioned element
list1 = ['hello', 'hi', 'thankyou', 'bye']
list1.remove('thankyou')
print(list1)

# pop() function
# removes an element on the basis of index
list2 = ['hi', 'hello', 'thankyou', 'bye']
# it will remove 'thankyou' (2nd index) from list
list2.pop(2)
print(list2)

# using pop() without an index
# this will remove the last element from the list
list2.pop()
print(list2)

# clear() function
# clears the whole list
list3 = ['hi', 'hello', 'thankyou', 'bye']
print('Initial : ', list3)
list3.clear()
print('Final : ', list3)

# del keyword
list4 = ['hi', 'hello', 'thankyou', 'bye']
print('Initial : ', list4)
# removing index 2
# removing 'thankyou' from the list
del list4[2]
print('Final : ', list4)


