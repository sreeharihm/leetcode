from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row = len(board)
        self.col = len(board[0])    
        self.board = board    
        for r in range(self.row):
            for c in range(self.col):
                if self.dfs(r,c,word):
                    return True
        return False
    
    def dfs(self,r,c,wd):
        if len(wd)==0:
            return True
        if(r<0 or r== self.row or c<0 or c==self.col or self.board[r][c]!= wd[0]):
            return False
        self.board[r][c]='#'
        for rowOffset,colOffset in [(0,1),(1,0),(0,-1),(-1,0)]:
            if(self.dfs(r+rowOffset,c+colOffset,wd[1:])):
                return True
        self.board[r][c] = wd[0]    
        return False



a = Solution()
print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))