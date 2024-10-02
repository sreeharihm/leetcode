from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)


    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val  and self.isMirror(t1.left,t2.right) and self.isMirror(t1.right , t2.left)

a = Solution()
node =TreeNode(1,None,None)

node.left = TreeNode(2,None,None)
node.left.left = TreeNode(4,None,None)
node.left.right = TreeNode(3,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)
node.right.right = TreeNode(4,None,None)

print(a.isSymmetric(node))