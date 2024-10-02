from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        if(r<1):
            return nums

        while(l<r):
            if(nums[l]%2!=0) and nums[r]%2==0:
                t = nums[l]
                nums[l] = nums[r]
                nums[r] =t
                l+=1
                r-=1
            elif nums[l]%2!=0 and nums[r]%2!=0:
                r-=1
            else:
                l+=1
        return nums

a = Solution()
print(a.sortArrayByParity([0]))