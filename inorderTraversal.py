from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # op = []
        # self.traversal(root,op)
        # return op
        res = []
        node = root
        nodes = []
        while node or nodes:
            if node:
                nodes.append(node)
                node = node.left
            else:
                node = nodes.pop()
                res.append(node.val)
                node = node.right
        return res
       
    
    def traversal(self,root: TreeNode, op):
        if root is None:
            return
        self.traversal(root.left,op)
        op.append(int(root.val))
        self.traversal(root.right,op)
        return

a = Solution()
tree =TreeNode(1,None,None)
tree.right = TreeNode(2,None,None)
tree.right.left = TreeNode(3,None,None)

print(a.inorderTraversal(tree))

        