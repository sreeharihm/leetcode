from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        count=0
        while(l<r):
            if nums[l]== nums[r]:
                