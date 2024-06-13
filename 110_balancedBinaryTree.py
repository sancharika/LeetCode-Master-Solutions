# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()
    
    def tree(self, tree_list):
        if not tree_list:
            return None
        self.root = TreeNode(tree_list[0])
        queue = [self.root]
        i = 1
        while i < len(tree_list) and queue:
            node = queue.pop(0)
            node.left = TreeNode(tree_list[i])
            queue.append(node.left)
            i += 1
            if i < len(tree_list):
                node.right = TreeNode(tree_list[i])
                queue.append(node.right)
                i += 1
        return self.root
                
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
T- O(n) S- O(n) (storing [balanced, height] for all node)
search from leaf node the abs differnce of left and right heigt
keep tab of balanced or not for each tres, left and right
create a recursuve dfs func which return [balanced T/F, height]

        """
        def dfs(root): #-> [bool,int(height)]
            #base case
            if not root: return [True,  0] #if not root consider true 
            left, right = dfs(root.left), dfs(root.right)
            #check balanced by 3 conditions:
            #1. left tree is balanced
            #2. right tree is balanced
            #3. abs height diff <=1
            balanced = (left[0] and right[0] and
            abs(left[1] - right[1])<=1)
            print(root.val)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(self.root)[0] #return if balanced of not
        
if __name__ == "__main__":
    root = [1,2,3,None,None,4]
    sol = Solution()
    root = sol.tree(root)
    print(sol.isBalanced(root)) #True