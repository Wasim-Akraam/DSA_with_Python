'Find the "Kth" max and min element of an List'
class Solution:
    def kthSmallest(self ,arr, l, r, k):
        '''
        arr : given List
        l : starting index of the List i.e 0
        r : ending index of the List i.e size-1
        k : find kth smallest element and return using this function
        '''

        arr.sort()

        return arr[ k -1]

obj=Solution()

print(obj.kthSmallest([7 ,10, 4, 3, 20, 15],0,6,4))