from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans =True
        
        def dfs(node):
            if node is None:
                return 0
            
            nonlocal ans
            l =dfs(node.left)
            r = dfs(node.right)

            if abs(l-r) > 1:ans =False

            return max(l,r)+1
        
        dfs(root)
        return ans
    
a = Solution()
node =TreeNode(1,None,None)

node.left = TreeNode(2,None,None)
node.left.left = TreeNode(4,None,None)
node.left.right = TreeNode(3,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)
node.right.right = TreeNode(4,None,None)

print(a.isBalanced(node))