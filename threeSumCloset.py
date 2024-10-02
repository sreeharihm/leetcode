import bisect
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                compliement = target-nums[i]-nums[j]
                hi = bisect.bisect_right(nums,compliement,j+1)
                lo = hi -1
                if hi< len(nums) and abs(compliement -nums[hi])<abs(diff):
                    diff = compliement-nums[hi]
                if lo> j and abs(compliement-nums[lo])<abs(diff):
                    diff = compliement-nums[lo]
                if diff==0:
                    break
        return target-diff
    
a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))

