#---------------------------- DELETED  FROM  LEETCODE -----------------------------
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        T- > Creating a new node O(n) + dfs O(n+e) traversing the nodes and edges S -> O(N)
DFS:
Take original nodes clone of it and cloning all of its neighbours recursively
appending created clone neighbour to the list of neighbours of the cur node

        """
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node] #already clone exist
            # no clone exist 
            copy = Node(node.val)
            #add to hashmap
            old_to_new[node] = copy

            #same for neghibours
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor)) #append clone of neihbours
            return copy

        return dfs(node) if node else None
    def print_graph(self, node):
        if node: return print(node.val)
        for neighbor in node.neighbors:
            self.print_graph(neighbor)


if __name__=="__main__":
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    s.cloneGraph(node1) # returns [[2,4],[1,3],[2,4],[1,3]]
    s.print_graph(node1)