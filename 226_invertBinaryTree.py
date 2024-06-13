# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        #swap tha values by left to right and right to left
        root.left, root.right = root.right, root.left

        #dfs for left and right
        self.invertTree(root.left)
        self.invertTree(root.right)
        #return right <- root ->left
        return root
    
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(root.val)
    print(root.left.val, root.right.val)
    print(root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)
    invert = Solution().invertTree(root)    
    print("----- Inverted Tree--------")
    print(invert.val)
    print(invert.left.val, invert.right.val)
    print(invert.left.left.val, invert.left.right.val, invert.right.left.val, invert.right.right.val)
        