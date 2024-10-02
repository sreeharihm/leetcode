import math
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0        
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1         
    
a = Solution()
node =TreeNode(1,None,None)

node.left = TreeNode(2,None,None)
node.left.left = TreeNode(4,None,None)
node.left.right = TreeNode(3,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)
node.right.right = TreeNode(4,None,None)

print(a.maxDepth(node))