from typing import List

class Solution:
     def getRow(self, rowIndex: int) -> List[int]:
        list1=[]
        for i in range(rowIndex+1):
            level=[]
            for j in range(i+1):
                if j==0 or j==i:
                    level.append(1)
                else:
                    level.append(list1[i-1][j-1]+list1[i-1][j])
            list1.append(level)
        return list1[-1]        
        
    

a = Solution()
print(a.getRow(5))