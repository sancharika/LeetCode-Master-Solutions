from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()
    
    def treeList(self, tree_list):
        if not tree_list: return None
        self.root = TreeNode(tree_list[0])
        idx = 1
        queue = [self.root]
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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
BFS- Level order trfaversal and append the last element of eacyh level

        """
        if not root: return []
        res = []
        q = deque([root])
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(val[-1])
        return res

if __name__=="__main__":
    sol = Solution()
    tree_list = [1,2,3,None,5,None,4]
    root = sol.treeList(tree_list)
    print(sol.rightSideView(root))

        