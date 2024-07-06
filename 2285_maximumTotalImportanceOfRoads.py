from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """
        T - (nlong + edges) s - O(n)
ides : map node: edge count -> sorted based on edge count
nodes can have 0 edges so beter to use array instead of map
node weight -> greedy based on no of edges node connects to
label it - 1 to n
note: node label doesnt matter we just want max sum of edges
ex:
 0 - 1 - 2
map = {0: 1, 1: 2, 2: 1}
sorted:
 nodes:  0 2 1
edge_c:  1 1 2
 label:  0 1 2

 res: 0 + 1 * 1 + 2 * 2 = 1 + 4 = 5
 so res += edge_c * label
        """

        # 1. edge counts
        edge_cnt = [0] * n
        for n1, n2 in roads:
            edge_cnt[n1] += 1
            edge_cnt[n2] += 1
        
        # 2. sort
        label = 1
        res = 0
        for count in sorted(edge_cnt):
            res += count * label
            label += 1
        print(edge_cnt)
        return res

if __name__ == "__main__":
    sol = Solution()
    n = 8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7],[3,5],[4,6]]
    print(sol.maximumImportance(n, roads))