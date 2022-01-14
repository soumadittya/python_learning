# intersection of two unsorted array
# two pointer approach

array1 = [4, 2, 6, 9, 10, 5]
array2 = [10, 15, 14, 6, 3, 4]
result = []
array1.sort()
array2.sort()

m = 0
n = 0

while(m < len(array1) and n < len(array2)):
    if(array1[m] == array2[n] and array1[m] not in result):
        result.append(array1[m])
        n = n + 1
        m = m + 1

    elif(array1[m] < array2[n]):
        m = m + 1

    else:
        n = n + 1

print('Result : ', result)


