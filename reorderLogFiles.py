from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            key =(0, rest, _id) if rest[0].isalpha() else (1, )
            print(key)
            return key

        item  = sorted(logs)
        return item
    
a = Solution()
print(a.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))