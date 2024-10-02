from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while(l<r):
            width =r-l
            area =max(area,min(height[l],height[r])*width)
            if height[l]<=height[r]:
                l=l+1
            else:
                r=r-1
        return area



a =Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))