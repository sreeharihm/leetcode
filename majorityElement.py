from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        result =0
        for i in nums:
            if count==0:
                result=i
            if i==result:
                count+=1
            else:
                count-=1    
        return result
        
a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))
