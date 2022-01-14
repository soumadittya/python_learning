# sorting lists

list1 = ['bob', 'ana', 'harry', 'john']
list1.sort()
print('list1 sorted : ', list1)

list2 = [2, 1, 9, 45, 34, 90, 23]
list2.sort()
print('list2 sorted : ', list2)

# sorting in reverse order
list3 = [90, 100, 70, 34, 23, 12, 8]
list3.sort(reverse = True)
print('list3 reversed sort : ', list3)

# custom sorting function
# key keyword
# Example : Sort the list based on how close the number is to 50
def myfunc(n):
    # returning the absolute value
    return abs(n - 50)
list5 = [100, 23, 76, 34, 90, 24]
list5.sort(key = myfunc)
print(list5)
