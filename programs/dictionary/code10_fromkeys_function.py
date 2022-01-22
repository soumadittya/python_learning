# other dictionary functions

# fromkeys() function
# tuple x contains all the keys
# y is the value for all the keys in tuple x
x = ('key1', 'key2', 'key3')
y = 0
dict1 = dict.fromkeys(x, y)
print("dict1 : ", dict1)

# tuple x contains all the keys
# tuple y is the value for all the keys
x = ('key1', 'key2', 'key3')
y = (1, 2, 3)
dict2 = dict.fromkeys(x, y)
print("dict2 : ", dict2)

