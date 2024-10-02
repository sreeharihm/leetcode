class Solution:
    def isPalindrome(self, s: str) -> bool:
        ip = s.lower()
        l=0
        r=len(ip)-1
        if r==0:
            return True
        while l<r:
            if not ip[l].isalnum():
                l+=1
            elif not ip[r].isalnum():
                r-=1
            elif (ip[l]!=ip[r]):
                return False
            else:
                l+=1
                r-=1
        return True
    
    
a=Solution()
print(a.isPalindrome(".,"))