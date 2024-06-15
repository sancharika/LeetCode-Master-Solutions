from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        T-> O(m*n) <- S (because of hashset)
        """
        area = 0
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r not in range(rows) or 
                c not in range(cols) or
                not grid[r][c] or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            #run dfs in all 4 directions
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) +
            dfs(r, c + 1) + dfs(r, c - 1)) 

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area
        
if __name__ == "__main__":
    grid = [ [0,0,1,0,0,0,0,1],
             [0,1,0,0,0,0,0,1],
             [0,1,1,1,1,1,1,0],
             [0,1,0,0,0,0,0,0],
             [0,1,1,1,1,1,1,0],
             [0,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,1]]
    
    print(Solution().maxAreaOfIsland(grid)) #15
