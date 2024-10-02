from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        i = len(digits)-1
        if digits[i]<9:
            digits[i]+=1
        else:
            while i>-1:               
                if digits[i]+carry>9:
                    digits[i]=0
                    carry=1  
                else:
                    digits[i] = digits[i]+carry
                    carry=0
                i-=1
            if carry==1:
                digits.insert(0,1)       
        return digits

a=Solution()
print(a.plusOne([4,3,2,1]))