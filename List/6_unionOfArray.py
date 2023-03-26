
def union(arr1,arr2):

    m=len(arr1)
    n=len(arr2)
    i,j=0,0

    while(i<m and j<n):
        if arr1[i]>arr2[j]:
            print(arr2[j],end=' ')
            j=j+1
        elif arr1[i] < arr2[j]:
            print(arr1[i], end=' ')
            i=i+1

        else:
            print(arr2[j],end=' ')
            i+=1
            j+=1

    while(i<m):
        print(arr1[i],end=" ")
        i+=1
    while (j<n):
        print(arr2[j],end=" ")
        j+=1


arr1=[10,2,3,4,5]
arr2=[5,6,7,8,9,8]

print(union(arr1,arr2))