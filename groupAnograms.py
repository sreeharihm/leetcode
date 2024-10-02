import collections
from typing import  List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count =[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            ans[tuple(count)].append(s)
        return ans.values()
        """ for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values() """
    
a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))