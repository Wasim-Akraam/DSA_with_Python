'Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo'


class Solution:
    def sort012(self,arr,n):
        # code here
        for i in range(n):
            for j in range(i,n-1):
                if arr[i]>arr[j+1]:
                    t=arr[i]
                    arr[i]=arr[j+1]
                    arr[j+1]=t
        return arr
obj=Solution()

ans=obj.sort012([0,1,2,2,0,0],6)
print(ans)

output=[0, 0, 0, 1, 2, 2]