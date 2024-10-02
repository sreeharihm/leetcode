class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        i=-1
        le =len(s)
        if(le==1):
            return 1
        while s:
            if(s[i]==' '):
                i-=1
            else:
                break

        while s:
            if(s[i]==' '):
                return l
            l+=1
            if(le+i==0):
                break
            i-=1
        return l
    
a =Solution()
print(a.lengthOfLastWord("  fly me   to   the moon  "))
