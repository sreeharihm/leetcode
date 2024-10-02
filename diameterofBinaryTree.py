from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            diameter = max(diameter,left_path+right_path)

            return max(left_path,right_path)+1

        longest_path(root)
        return diameter
    
a = Solution()
tree =TreeNode(-10,None,None)
tree.left = TreeNode(9,None,None)
tree.right = TreeNode(20,None,None)
tree.right.left = TreeNode(15,None,None)
tree.right.right = TreeNode(7,None,None)
print(a.diameterOfBinaryTree(tree))