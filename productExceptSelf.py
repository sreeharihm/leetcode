from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        op = [0]*length
        op[0]=1
        r=1
        for i in range(1,length):
           op[i]= op[i-1]*nums[i-1]
        for i in reversed(range(length)):
           op[i]= op[i]*r
           r*=nums[i]
        return op
    
a= Solution()
print(a.productExceptSelf([1,2,3,4]))
