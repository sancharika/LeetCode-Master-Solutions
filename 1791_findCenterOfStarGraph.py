from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        T - O(n) - S
calculate number of edge each node has
find node which has edge count ==  len of edges
The center is the only node that has more than one edge.
and is also connected to all other nodes.

trick -> T- O(1) [only checking first 2 elemenst of edges] S - O(1) [no extra memory]
first node == second edge node[0] or [1] then first node[0] is the center node else first node[1]
if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] then center = edges[0][0] else edges[0][1]
cos every list of edges will have center node as center node connects to all so either one of the first list is center
in order to find which one the trick is:
if first list[0] present in next list then thats the center else its first list[1]
        """
        # graph = {}
        # for edge in edges:
        #     graph[edge[0]] = graph.get(edge[0], 0 ) + 1
        #     graph[edge[1]] = graph.get(edge[1], 0 ) + 1
        # print(graph)
        # for node, count in graph.items():
        #     if len(edges) == count:
        #         return node
        # return -1
        #s -O(1)
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
    
if __name__ == "__main__":
    edges = [[1,4],[4,3],[4,2]]
    print(Solution().findCenter(edges))