from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
Time Complexity: O(n)
Space Complexity: O(n) in the worst case, O(log(n)) in the best case
        """
        value = root.val
        def dfs(node):
            if not node: return True
            
            if node.val != value: return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
            
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    print(solution.isUnivalTree(root)) # True