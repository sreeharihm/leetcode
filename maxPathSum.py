from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        def get_subtree(node)-> int:
            nonlocal max_path
            if node is None:
                return 0
            gain_left = max(get_subtree(node.left),0)
            gain_right = max(get_subtree(node.right),0)

            current_max_path = node.val + gain_left +gain_right
            max_path = max(max_path,current_max_path)
            return max(gain_left+node.val, gain_right +node.val)

        get_subtree(root)
        return max_path

a = Solution()
tree =TreeNode(-10,None,None)
tree.left = TreeNode(9,None,None)
tree.right = TreeNode(20,None,None)
tree.right.left = TreeNode(15,None,None)
tree.right.right = TreeNode(7,None,None)
print(a.maxPathSum(tree))

        
          