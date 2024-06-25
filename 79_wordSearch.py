from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
Recursive backtracking: O(r*c*dfs) T of dfs- O(4*len(word))
check if cur word present in cur cell and next in neighbour cells
        """

        rows, cols = len(board), len(board[0])
        visit = set()
        #arg: cur row, cur col, cur idx of word
        def dfs(r, c, idx):
            #check if out of bound and not in word[idx]
            if (0 > r or r >= rows or c < 0 or 
            c >= cols or board[r][c] != word[idx] or
            (r,c) in visit): return False
            #if last index of word then word present in board 
            if idx == len(word)-1: return True 
            visit.add((r,c)) #we found 1 needed charcters
            #search in neighbour for next word
            res = (dfs(r + 1,c, idx + 1) or
            dfs(r - 1,c, idx + 1) or
            dfs(r, c + 1, idx + 1) or
            dfs(r, c - 1, idx + 1))
            # remove visit to explore other paths
            visit.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        #in not found    
        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(Solution().exist(board, word)) #True