from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op= []
        def solve(str,l,r,n):
            if len(str)== 2*n:
                op.append(str)
            if l<n:
                temp=str
                temp =temp+"("
                solve(temp,l+1,r,n)
            if r<l:
                temp=str
                temp = temp+")"
                solve(temp,l,r+1,n)
        solve("",0,0,n)
        return op

a = Solution()
print(a.generateParenthesis(3))