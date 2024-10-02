from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        map = Counter(s)
        op=""
        for ch in s:
            if map[ch]!=1:
                map[ch]-=1
            else:
                op+=ch
        return op


s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))