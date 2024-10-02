class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x%10==0 and x!=0:
            return False
        z=x
        y=0
        while x>0:  
            y=y*10+x%10        
            x=x//10                       
        return (y==z)
a = Solution()
print(a.isPalindrome(121))
'''
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Time complexity - O(log(n))
Space complexity- O(n)
'''