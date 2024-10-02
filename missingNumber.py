from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        map= set(nums)
        n = len(nums)+1
        for i in range(n):
            if i not in map:
                return i

""" n = len(nums)
summ = int((n * (n+1))/2)
ans = summ - sum(nums) """

""" missing = len(nums)
for i, num in enumerate(nums):
    missing ^= i ^ num
return missing """

a = Solution()
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))