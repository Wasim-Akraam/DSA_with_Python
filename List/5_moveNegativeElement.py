"Move all the negative elements to one side of the List "

def rearrangement(arr):
    for j in range(len(arr)):
        for i in range(len(arr)):
            if (arr[i]>0):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

    return arr
arr=[-1,2,3,4,-9]
print(rearrangement(arr))













    