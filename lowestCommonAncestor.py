class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node):
            if node is None:
                return None
            if node == p or node ==q:
                return node
            left = traverse(node.left)
            right = traverse(node.right)

            if left and right:
                return node
            return left or right
        return traverse(root)
    
a = Solution()
tree =TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)
p =TreeNode(5)
q =TreeNode(1)
print(a.lowestCommonAncestor(tree,p,q))
