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
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
traverse in order and pop the element until its k
poping element will be in sorted order only
traverse in stack to keep track of nodes and curr node
basiccaly goinf as far left as possible adding value to stack 
then poping it out and a
        """
        #number of nodes visited return node.val whene n==k
        stack = [] #iterate through node
        cur = root #current pointer
        #while curremt not nul and stack not empty
        while cur or stack:
            while cur:
                #keep track of nodes thats needs to be procesed after left
                stack.append(cur)
                #keep going left before processing cur
                cur = cur.left
            #here it means cur is none and processed left so remove most current node
            cur = stack.pop()
            k -= 1 #just visited the cur node
            if k==0: return cur.val #will always executive
            cur = cur.right #already processed all left so not visit right

if __name__ == "__main__":
    tree_list = [5,3,6,2,4,None,None,1]
    sol = Solution()
    root = sol.treeList(tree_list)
    print(sol.kthSmallest(root, 3)) #output: 3

        