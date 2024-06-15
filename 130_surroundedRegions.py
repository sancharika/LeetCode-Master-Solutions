from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        T-> O(m*n) DFS-> O(N+E)  S-> O(max(n,m)) (for dfs) + O(1)
Three steps:
1. DFS: Find unsurronded graph aka "O" in borderlines and replace them with Temp name
 - for all boundaries r in [0, rows-1] and c in [0, cols - 1]
2. Replace all the "O" with "X" because now all the "O"s are valid and surrounded by "X"
3. Find cells with Temp name and replace them with "O"
        """
        rows, cols = len(board), len(board[0])

        #dfs to replace O to T
        def dfs(r, c):
            if (r not in range(rows) or
            c not in range(cols) or
            board[r][c] != "O"
            ): return
            board[r][c] = "T"
            #chck for adjacent "O"s
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            ##or can do this
            # directions = [[0,1], [0,-1,],[1, 0],[-1,0]]
            # for dr, dc in directions:
            #     dfs(r + dr, c+dc)

        #1. find boundary "O" and replace it with T
        for r in range(rows):
            for c in range(cols):
                # find "O" in boundary 
                if board[r][c] == "O" and (r in [0, rows -1]
                or c in [0, cols-1]):
                    dfs(r, c) #replace boundary "O"s with T

        #2. replace O with X
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c] = "X"
                #3. replace T with O
                elif board[r][c]=="T":
                            board[r][c] = "O"

if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)
    print(board)
