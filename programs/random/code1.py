# union using set data structure

array1 = [4, 2, 6, 9, 10, 5]
array2 = [10, 15, 14, 6, 3, 4]

# creating an empty set
myset = set()

# populating the set with unique values of array1 and array2
myset.update(array1)
myset.update(array2)

print('Union : ', myset)

