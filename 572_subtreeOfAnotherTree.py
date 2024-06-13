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
            node.left  = TreeNode(tree_list[idx])
            queue.append(node.left)
            idx += 1
            if idx < len(tree_list):
                node.right = TreeNode(tree_list[idx])
                queue.append(node.right)
                idx += 1
        return self.root


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #T - O(tree * sub root tree)
        #if sub tree null and root tre not nul then true not vice versa
        if not subRoot: return True
        if not root: return False
        #if same return true
        if self.sameTree(root, subRoot): return True
        #check if root.left or root. right subtree of subroot then return True
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))



        #compare 2 trees
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if both null return true
        if not root and not subRoot: return True
        #if root and subroot exists and same value recursion for left and right
        # root and sub root
        if root and subRoot and root.val == subRoot.val: 
            return (self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right))
        #if it comes here either null root or subroot or != values return false
        return False

if __name__=="__main__":
    tree_list = [3,4,5,1,2]
    sub_tree_list = [4,1,2]
    sol = Solution()
    root = sol.treeList(tree_list)
    subRoot = sol.treeList(sub_tree_list)
    print(sol.isSubtree(root, subRoot)) #True
        