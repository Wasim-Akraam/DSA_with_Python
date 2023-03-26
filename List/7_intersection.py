def intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    for i in range(m):
        for j in range(n):
            if (arr1[i] == arr2[j]):
                print(arr1[i], end=' ')


arr1 = [1, 2, 5, 6]
arr2 = [2, 3, 5, 6, 6]
print(intersection(arr1, arr2))

