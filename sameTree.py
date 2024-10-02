from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p== None or q ==None:
            return p==q
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
a = Solution()
node =TreeNode(1,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)

node1 =TreeNode(1,None,None)
node1.right = TreeNode(2,None,None)
node1.right.left = TreeNode(3,None,None)

print(a.isSameTree(node,node1))


# Tree 1
#     1
#    / \
#   2   3

# Tree 2
#     1
#    / \
#   2   3

# Output: True

# Tree 1
#     1
#    / \
#   2   3

# Tree 2
#     1
#    / \
#   2   4

# Output: False