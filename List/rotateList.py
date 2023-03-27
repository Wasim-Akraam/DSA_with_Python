"Write a program to cyclically rotate an array by one."


def rotate( arr, n):
    b=arr.pop(n-1)
    arr.insert(0,b)
    return arr

N = 5
A= [1, 2, 3, 4, 5]

print(rotate(A,N))