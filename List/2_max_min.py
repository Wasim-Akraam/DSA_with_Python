
"""  Find the maximum and minimum element in an List """


def max_min(a):
    minimum = a[0]
    maximum = a[0]

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                minimum = a[j + 1]

            else:
                maximum = a[j + 1]

    print("Maximum value in given list :", maximum)
    print("minimum value in given list :", minimum)


max_min([3, 6, 99, 110])