from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}  # Create an empty dictionary 

        # Iterate through each element in nums
        for i in nums:
            if i not in dict:  # If the element is not in the dictionary
                dict[i] = True  # Add it to the dictionary with a value of True
            else:
                dict[i] = False  # If the element already exists in the dictionary, set its value to False

        # Iterate through the key-value pairs in the dictionary
        for key, val in dict.items():
            if val == True:  # If the value is True (indicating a single occurrence)
                return key  # Return the corresponding key as the single number

    
a = Solution()
print(a.singleNumber([4,1,2,1,2]))
                    
