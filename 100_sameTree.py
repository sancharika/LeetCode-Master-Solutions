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
        if not tree_list:
            return None
        self.root = TreeNode(tree_list[0])
        queue = [self.root]
        idx = 1 
        while idx < len(tree_list):
            node = queue.pop(0)
            node.left = TreeNode(tree_list[idx])
            queue.append(node.left)
            idx += 1
            if idx < len(tree_list):
                node.right = TreeNode(tree_list[idx])
                queue.append(node.right)
                idx += 1
        return self.root


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #T- O(p+q) S- O(h), where h is the height of the trees; in the worst case, O(n)
        #base case
        #if both null then consider true
        if not p and not q: return True
        #if either of them is nullor not same value return false
        if not p or not q or p.val != q.val: return False
        #chck for p and q left and p and q right if both true then true else false
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
    

if __name__ == "__main__":
    tree_list1 = [1,2,3]
    tree_list2 = [1,2,None,3]
    sol = Solution()
    p = sol.treeList(tree_list1)
    q = sol.treeList(tree_list2)
    print(sol.isSameTree(p, q))

        