from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        
        #take hashmap for col ros and sqaure
        col = defaultdict(set)
        row = defaultdict(set) # {i: [1...9]}
        square = defaultdict(set) # key = (r//3)(c//3) for 3 x 3 subset


        for r in range(9):
            for c in range(9):
                #continue if empty
                if board[r][c] == ".":
                    continue
                # if [r][c] already exist not valid
                #check in row r col c sq r//3,c//3
                if (board[r][c] in row[r] or 
                board[r][c] in col[c] or 
                board[r][c] in square[(r//3,c//3)]):
                    return False
                # add value to set not append
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        #if for loop exits no duplicate found
        return True
                

if __name__=="__main__":
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
        ]
    print(Solution().isValidSudoku(board))

