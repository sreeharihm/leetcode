from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x= len(image)
        y = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color: return image
        def dfs(r,c):
            if image[r][c]== oldColor: 
                image[r][c] = color
                if c>=1: dfs(r,c-1)
                if r>=1: dfs(r-1,c)
                if c+1<y: dfs(r,c+1)
                if r+1<x: dfs(r+1,c)
        
        dfs(sr,sc)

        return image




a= Solution()
print(a.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))