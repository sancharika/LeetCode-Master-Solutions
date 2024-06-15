from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        T -> O(n*M) <-S
        DFS - S-> O(max(m,n)) T-> O(N+E) 
search possible cells for pacific and Atlantic return the index of its union
dfs to add adjacent possible cells to the visisted set 
dfs func-> arg(row, col, visited set, previous height)
        """
        rows, cols = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        res = []

        #dfs 
        def dfs(r, c, visit, prev_height):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                heights[r][c] < prev_height
            ): return #we need max height not less
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        # dfs for top and bottom row
        for c in range(cols):
            #top in pacific
            dfs(0, c, pacific, heights[0][c])
            #bottom in atlantic
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        #for left and right col
        for r in range(rows):
            #left in pacific
            dfs(r, 0, pacific, heights[r][0])
            #right in atlantic
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        # common in pacific and atlantic set
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
        
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(heights)) # [[0, 4], [1, 3], [1, 4], [2, 2], [3 , 0], [3, 1], [4, 0]]

        