class Solution:
    def climbStairs(self, n: int) -> int:
        o,t=1,1
        for _ in range(n-1):
            o,t= t,o+t
        return t 
    
a =Solution()
print(a.climbStairs(4))

