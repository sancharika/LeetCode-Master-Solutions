from typing import Optional
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
        queue = [self.root]
        idx = 1
        while idx < len(tree_list):
            node = queue.pop(0)
            if tree_list[idx]: node.left = TreeNode(tree_list[idx])
            if node.left: queue.append(node.left)
            idx += 1
            if idx < len(tree_list):
                if tree_list[idx]: node.right = TreeNode(tree_list[idx])
                if node.right: queue.append(node.right)
                idx+=1
        return self.root
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #T - O(n) S-O(1)
        def valid(left, node, right):
            #empty tree can be considerd binary tree
            if not node: return True
            if not (left < node.val < right): return False
            #for left tree compare btw root and node.left
            #ex -inf< node.left<node so left can remain unchanged
            #for right right can remain unchanged
            #ex root < node.right < inf
            return (valid(left, node.left , node.val) and
            valid(node.val, node.right, right))
        return valid(float("-inf"), root, float("inf"))
    
if __name__ == "__main__":
    tree_list = [2,1,3]
    sol = Solution()
    root = sol.treeList(tree_list)
    print(sol.isValidBST(root)) #True