arr1 = [2, 6, 9, 11, 13, 17]
arr2 = [3, 6, 7, 10, 13, 18]
arr3 = [4, 5, 6, 9, 11, 13]

i = 0
j = 0
k = 0
result = []
while (i < len(arr1)) and (j < len(arr2)) and (k < len(arr3)):
    if arr1[i] == arr2[j] == arr3[k]:
        result.append(arr1[i])
        i += 1
        j += 1
        k += 1
    elif arr1[i] < arr2[j]:
        i += 1
    elif arr2[j] < arr3[k]:
        j += 1
    else:
        k += 1
