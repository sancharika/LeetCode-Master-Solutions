# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### functional approach
class Solution:

    # print the tree
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.print_tree(node.left, level + 1)
            
    
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        T - O(n) [going trhough all nodes of tree] S - O(1)[in place value]
order -> Right, Node, Left
keep track of cur sum using global variable
Recursively call on the right subtree.
Update the current node's value by adding the val to it.
Recursively call on the left subtree.
if using total:
    return the total for each call and modify the toal accordingly 
    then you dont need global val
        """
        def dfs(node, total):
            
            if node.right: total = dfs(node.right, total) 
            total += node.val
            node.val = total
            if node.left: total = dfs(node.left, total)
            return total
        dfs(root, 0)
        return root

### using class variables 
# class Solution:
#     def __init__(self):
#         self.val = 0

#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         def dfs(node):
#             if not node:
#                 return None
            
#             dfs(node.right)
#             self.val += node.val
#             node.val = self.val
#             dfs(node.left)

#         dfs(root)
#         return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    print("BST:")
    Solution().print_tree(root)
    root = Solution().bstToGst(root) # returns [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    print("GST:")
    Solution().print_tree(root)
            

