from typing import List
class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
       hashmap= {}
       for i in range(len(nums)):
           compliment = target -nums[i]
           if compliment in hashmap:
               return [i, hashmap[compliment]]
           hashmap[nums[i]] = i

a = Solution()
print(a.twosum([3,2,4],6))
'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Time complexity - O(n)
Space complexity- O(n)
'''
