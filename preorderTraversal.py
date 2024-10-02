from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ op = []
        self.traversal(root,op)
        return op """
        res = []
        stack=[root]
        while stack:
           node= stack.pop()
           res.append(node.val)
           if node.left:
               stack.append(node.left)
           if node.right:
               stack.append(node.right)
        return res 
       
    
    def traversal(self,root: TreeNode, op):
        if root is None:
            return
        
        op.append(int(root.val))
        self.traversal(root.left,op)
        self.traversal(root.right,op)
        return

a = Solution()
tree =TreeNode(1,None,None)
tree.right = TreeNode(2,None,None)
tree.right.left = TreeNode(3,None,None)

print(a.preorderTraversal(tree))

        