class Solution:
    def romanToInt(self,s: str) -> int:
        res = {"I":1 ,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        op=0
        for i in range(len(s)):
            if((i+1)<len(s) and res[s[i]]<res[s[i+1]]):
                op-=res[s[i]]
            else:
                op+=res[s[i]]
        return op
    

a = Solution()
print(a.romanToInt("MCMXCIV"))       

'''
Example 1:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
Time complexity - O(n)
Space complexity- O(n)
'''