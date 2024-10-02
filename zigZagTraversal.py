from collections import deque
from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        results =[]

        def dfs(node, level):
            if level >=len(results):
                results.append(deque([node.val]))
            else:
                if level%2==0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left,node.right]:
                if next_node is not None:
                    dfs(next_node,level+1)
        dfs(root,0)
        return results
    
a= Solution()
tree =TreeNode(3,None,None)
tree.left = TreeNode(9,None,None)
tree.right = TreeNode(20,None,None)
tree.right.left = TreeNode(15,None,None)
tree.right.right = TreeNode(7,None,None)
print(a.zigzagLevelOrder(tree))