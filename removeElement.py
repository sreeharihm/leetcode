from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)    

a = Solution()
print(a.removeElement([3,2,2,3],3))         