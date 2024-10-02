from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q= []
        if root is None:
            return 0
        
        q.append({"node": root,"depth":1})

        while len(q)>0:
            queueItem = q.pop(0)

            node = queueItem["node"] 
            depth = queueItem["depth"]

            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                q.append({"node": node.left,"depth":depth+1})
            if node.right is not None:
                q.append({"node": node.right,"depth":depth+1})

a = Solution()
node =TreeNode(1,None,None)

node.left = TreeNode(2,None,None)
node.left.left = TreeNode(4,None,None)
node.left.right = TreeNode(3,None,None)
node.right = TreeNode(2,None,None)
node.right.left = TreeNode(3,None,None)
node.right.right = TreeNode(4,None,None)

print(a.minDepth(node))