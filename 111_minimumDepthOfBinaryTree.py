from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = None

    def treeList(self, tree_list: List[Optional[int]]) -> Optional[TreeNode]:
        if not tree_list:
            return None
        
        self.root = TreeNode(tree_list[0])
        queue = [self.root]
        index = 1
        
        while index < len(tree_list):
            node = queue.pop(0)
            if index < len(tree_list) and tree_list[index] is not None:
                node.left = TreeNode(tree_list[index])
                queue.append(node.left)
            index += 1
            if index < len(tree_list) and tree_list[index] is not None:
                node.right = TreeNode(tree_list[index])
                queue.append(node.right)
            index += 1
            
        return self.root

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        T - O(n) S- O(h), where h is the height of the tree, which can be O(n) in the worst case and O(\log n) in the best case.
        min height of tree starting from leaf node 
        consider if empty left then min depth for right only or vice versa
        """
        if not root:
            return 0  # if no node
        if not root.left and not root.right:
            return 1  # if 1 node with no left and right node
        if not root.left:
            return self.minDepth(root.right) + 1  # if none left node then recursion for right node + curr node to right node edge
        if not root.right:
            return self.minDepth(root.left) + 1  # if none right then min depth for left
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# Example usage
sol = Solution()
tree_list = [3, 9, 20, None, None, 15, 7]
root = sol.treeList(tree_list)
min_depth = sol.minDepth(root)
print(f"Minimum Depth: {min_depth}")
