from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ##if none roort return 0
        if not root: return 0
    ##Recursive DFS T-> O(n) S->O(height) worst case O(n)
        ## sum the max of left and right with root node        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    ##Avoid recursion BFS T-> O(n) S->O(height) worst case O(n)
    ## BFS using queue
        
        ##start with level 0
        # level = 0
        ##convert tree to queue start with root
        # queue = deque([root])
        ## while queue is true iterater through that level
        ## for queue in that level pop left and add root.left or root.right if exist
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         #add the entire node left of poped one if exists 
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     # once outside the loop 1 level completes
        #     level += 1
        # return level

    ## Iterative DFS
    ## pre order dfs using stack
        # take stack which has [node, depth]
        stack = [[root,1]]
        res = 0
        while stack:
            #pop the curr node and chck if  it has child or not
            node, depth = stack.pop()
            if node: #if node not none then its in next level
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth(root)) #3
