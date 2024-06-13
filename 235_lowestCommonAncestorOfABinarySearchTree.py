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
            
            if node is not None:
                left_value = tree_list[idx]
                if left_value is not None:
                    node.left = TreeNode(left_value)
                queue.append(node.left)
                idx += 1
                
                if idx < len(tree_list):
                    right_value = tree_list[idx]
                    if right_value is not None:
                        node.right = TreeNode(right_value)
                    queue.append(node.right)
                    idx += 1
        
        return self.root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #T - O(height) -> O(logn) S-O(1)
        while True:
            # if p > root and q> root then go right
            if p.val > root.val and q.val > root.val:
                root = root.right
            # if p and q < root go left side
            elif p.val < root.val and q.val < root.val:
                root = root.left 
            #else finding p or q 
            else: return root #it will execute always
        
if __name__ == "__main__":
    sol = Solution()
    tree_list = [6,2,8,0,4,7,9,None,None,3,5]
    root = sol.treeList(tree_list)
    p = TreeNode(2)
    q = TreeNode(8)
    print(sol.lowestCommonAncestor(root, p, q).val) #3
