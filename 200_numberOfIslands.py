from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
iterative bfs BFS to find adjacent islands
BFS-> queue and visited to expand island
use direction to find adjacent islands:
right [1, 0]
left [-1, 0]
above [0, 1]
below [0, -1]
in loop check:
1. adjacent rows, cols in bound
2. cur position is land -> grid[][]==1
3. not visited
on true for above add to queue and visited as they are part of bfs graph 

        """
        #if empty grid
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        # #bfs
        # def bfs(r,c):
        #     q = deque([(r,c)]) #queue stores tuple (row,col)
        #     visit.add((r, c))
        #     while q:
        #         row, col = q.popleft() # if pop instead of popleft then pop recent update
                                            # making it iterative dfs
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #         for dr, dc in directions:
        #             cur_r, cur_c = row + dr, col + dc
        #             if (cur_r in range(rows) and
        #             cur_c in range(cols) and
        #             grid[cur_r][cur_c] == "1" and
        #             (cur_r, cur_c) not in visit
                    
        #             ):
        #                 q.append((cur_r, cur_c))
        #                 visit.add((cur_r, cur_c))

        #dfs
        def dfs(r, c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != "1" or
                (r, c) in visit
            ): return
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # bfs(r,c) #bfs
                    dfs(r, c) #dfs
                    island += 1 #increment island count
        return island
    
if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","0"]
        ]
    
    print(Solution().numIslands(grid)) #output: 1