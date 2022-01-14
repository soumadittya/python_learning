# accessing list

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# first item
print(list1[0])

# last item
print(list1[-1])

# second last item
print(list1[-2])

# third, fourth and fifth item
# from 2nd index to 4th index (but not 5th index)
print(list1[2 : 5])

# 4th index to 9th index
print(list1[4 : ])
# or
print(list1[4 : 10])

# 4th index to 8th index
print(list1[4 : 9])

# from 0th index to 4th index
print('0th index to 4th index : ', list1[0 : 5])
# or
print(list1[ : 5])

# for searching from end of the list
# we need to make use of -ve index

# from 4th last to 2nd last
# this will include index -4 to index -2 (but not index -1)
print('From 4th last to 2nd last : ', list1[-4 : -1])

# from 4th last to last
print('4th last to last : ', list1[-4 : ])



