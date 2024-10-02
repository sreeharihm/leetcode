from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = Counter(s)
        for i,a in enumerate(s):
            if hashMap[a]==1:
                return i 
        return -1


a =Solution()
print(a.firstUniqChar("loveleetcode"))
            