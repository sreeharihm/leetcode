from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[]
        node=root
        while node or stack:
            if node:
                stack.append(node)
                ans.append(node.val)
                node=node.right
            else:
                node=stack.pop()
                node=node.left
        return ans[::-1]


a = Solution()
tree =TreeNode(1,None,None)
tree.right = TreeNode(2,None,None)
tree.right.left = TreeNode(3,None,None)

print(a.postorderTraversal(tree))
