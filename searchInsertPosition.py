from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        m=0
        while l<r:
            m=(l+r)//2
            if(nums[m]> target):
                r=m
            elif(nums[m]< target):
                l=m+1
            elif(nums[m]==target):
                return m
        return r

a= Solution()
print(a.searchInsert([1,3,5,6],5))