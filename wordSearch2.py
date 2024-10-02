from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        matching= []
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])

        def dfs(r,c,wd):
            letter = board[r,c]
            curNode = wd[letter]

            word_match = curNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matching.append(word_match)

            if len(wd)==0:
                return wd
            if(r<0 or r== self.row or c<0 or c==self.col or self.board[r][c]!= wd[0]):
                return False
            self.board[r][c]='#'
            for rowOffset,colOffset in [(0,1),(1,0),(0,-1),(-1,0)]:
                if(self.dfs(r+rowOffset,c+colOffset,wd[1:])):
                    return True
            self.board[r][c] = wd[0]    
            return wd
        for a in range(rowNum):
            for b in range(colNum):
                dfs(rowNum,colNum,trie)
        return matching

    



a = Solution()
print(a.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))