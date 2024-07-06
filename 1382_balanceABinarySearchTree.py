# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
create inorder list  -> dfs from left for getting sorted
use that list to create bst -> from mid, left, right
        """
        inorder = []

        def dfs(node):
            if not node: return
            
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        def balanced_bst(start, end):
            #if out of bound or crossed
            if start > end:
                return None
            
            mid = (start + end) // 2
            #left bst
            left = balanced_bst(start, mid - 1)
            #right bst
            right = balanced_bst(mid + 1, end)
            #new node
            node = TreeNode(inorder[mid], left, right)
            return node
        dfs(root)
        #balanced bst
        bst = balanced_bst(0, len(inorder) - 1)
        return bst

    # print binary search tree
    def print_bst(self, node, level=0):
        if node is not None:
            self.print_bst(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.print_bst(node.left, level + 1)
    


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    s = Solution()
    res = s.balanceBST(root)
    Solution().print_bst(res)
    

        