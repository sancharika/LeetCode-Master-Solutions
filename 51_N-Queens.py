from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
search for possible n options to place queen in
after placing 1 queen check col row 2 diagonal to place another
positive diagonal: r+c constant ↗
negative diagonal: r-c constant ↘
        """

        col = set()
        pos_diagonal = set()
        neg_diagonal = set()
        res = []

        board = [["."] * n for i in range(n)]
        def backtrack(r): #take arg row
            #if row reached n
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            #for col check if it can be used or not
            for c in range(n):
                if c in col or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue

                #if its a valid cell
                col.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1) # backtrack for next row

                #remove valid cell to explore more options
                col.remove(c)
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)
                board[r][c] = "."
        #start backtrack
        backtrack(0)
        return res
        
if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4)) # [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]