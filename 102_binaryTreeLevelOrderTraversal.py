# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()
    
    def treeList(self, tree_list):
        if not tree_list:
            return None
        self.root = TreeNode(tree_list[0])
        queue = [self.root]
        idx =  1
        while idx < len(tree_list):
            node = queue.pop(0)
            if tree_list[idx]: node.left = TreeNode(tree_list[idx])
            if node.left: queue.append(node.left)
            idx += 1
            if idx < len(tree_list):
                if tree_list[idx]: node.right = TreeNode(tree_list[idx])
                if node.right: queue.append(node.right)
                idx += 1
        return self.root


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        T- O(n) (all node processed during traversal)
        S - O(n) (queue and res store n elements at worst)
        Use BFS algo and queue data strcuture for each level
        """
        res = []
        queue = [root] if root else []
        while queue:
            val = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                val.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(val)
        return res
            

if __name__ == "__main__":
    tree_list = [3,9,20,None,None,15,7]
    sol = Solution()
    root = sol.treeList(tree_list)
    print(sol.levelOrder(root)) # [[3], [9, 20], [15, 7]]