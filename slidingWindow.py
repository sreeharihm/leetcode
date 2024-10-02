from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l,r = 0,0
        formed =0
        windows_count = {}
        ans = float("inf"),None,None
        while r<len(s):
            character = s[r]
            windows_count[character] = windows_count.get(character,0)+1
            
            if character in dict_t and windows_count[character] == dict_t[character]:
                formed+=1
            
            while l<=r and formed ==required:
                character = s[l]
                if r-l+1 < ans[0]:
                    ans =(r-l+1,l,r)
                windows_count[character]-=1
                if character in dict_t and windows_count[character]< dict_t[character]:
                    formed-=1
                l+=1
            r+=1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
    
a = Solution()
print(a.minWindow("ABCDDDDDDEEAFFBC","ABC"))