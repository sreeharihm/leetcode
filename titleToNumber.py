class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        op=0
        l=len(columnTitle)-1
        for i in columnTitle:
            op=op+(ord(i)-ord("A")+1) *pow(26,l)
            l-=1
        return op

a = Solution()
print(a.titleToNumber("ZY"))