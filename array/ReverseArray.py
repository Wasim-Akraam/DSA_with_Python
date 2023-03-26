def reverseArray(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]<arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


A=[6,8,2,3,8,9]

print(reverseArray(A))