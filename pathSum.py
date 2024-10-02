from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [[root,root.val]]

        while stack:
            node, total = stack.pop()
            if total == targetSum and node.left is None and node.right is None:
                return True
            if node.right: stack.append([node.right,total+node.right.val])
            if node.left: stack.append([node.left,total+node.left.val])
        return False
    

a = Solution()
node =TreeNode(1,None,None)

node.left = TreeNode(2,None,None)
node.left.left = TreeNode(4,None,None)
node.left.right = TreeNode(3,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)
node.right.right = TreeNode(4,None,None)

print(a.hasPathSum(node,7))

