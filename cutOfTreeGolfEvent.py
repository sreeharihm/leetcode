import collections
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        x,y = len(forest),len(forest[0])
        def bfs(sr,sc,tr,tc):
            que = collections.deque([(sr,sc,0)])
            seen= {(sr,sc)}
            while que:
                r,c,d = que.popleft()
                if r == tr and c ==tc:
                    return d
                for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0<=nr<x and 0<=nc<y and (nr,nc) not in seen and forest[nr][nc]:
                        seen.add((nr,nc))
                        que.append((nr,nc,d+1))
            return -1
    
        toVisit= []
        for i in range(0,x):
            for j in range (0,y):
                if forest[i][j]>1:
                    toVisit.append((i,j))
        toVisit.sort()

        ans =0
        sx,sy =0,0
        for tx,ty in toVisit:
            d = bfs(sx,sy,tx,ty)
            if d==-1:
                return -1
            ans+=d
            sx,sy = tx,ty
        return ans




a = Solution()
print(a.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))