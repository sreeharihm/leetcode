from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map = Counter(s)

        for ch in t:
            if ch not in map or map[ch]==0:
                return ch
            else:
                map[ch]-=1


s = Solution()
print(s.findTheDifference("a","aa"))