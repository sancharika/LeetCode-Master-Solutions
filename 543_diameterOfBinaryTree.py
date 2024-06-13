# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
search the height of the tree from leaf node and add left
height and right height to get tree depth
left height + right height + 2 (edge connecting 
curr node to its left and right trees)
        """
        #global result
        res = 0
        def dfs(root):
            nonlocal res
            #it not root return -1 as 0 is for 1th root
            if not root: return  -1
            #left height
            left = dfs(root.left)
            #right height
            right = dfs(root.right)
            #max depth
            res = max(res, left + right + 2)

            return 1 + max(left, right) #return height of the tree

        dfs(root)
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    print(Solution().diameterOfBinaryTree(root)) #3