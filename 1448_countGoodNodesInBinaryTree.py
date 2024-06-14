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
    
    def goodNodes(self, root: TreeNode) -> int:
        """
consider root val as max then iterate through tree 
if node.val > max val add 1
dfs func with node and max val as arg
        """
        def dfs(node, max_val):
            if not node: return 0
            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        return dfs(root, root.val)
        
if __name__ == "__main__":
    tree_list = [3,1,4,1,5,9,2,6]
    sol = Solution()
    root = sol.treeList(tree_list)
    print(sol.goodNodes(root)) # 4
        