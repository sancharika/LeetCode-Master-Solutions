from typing import List
# import functools
import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
DP with memoization
T -> O(R*C) <- S [(r, c) is processed once, and memoization ]
calculates the length of the longest increasing path starting from the current cell by checking all four possible directions
 maximum length from the four possible directions, and 1 is added to include the current cell itself in the path length
        """
        R = len(matrix)
        C = len(matrix[0])
        
        @functools.cache
        def util(r, c):
            if r < 0 or c < 0  or r >= R or c >= C:
                return 0
            
            val = matrix[r][c]
            return 1 + max([
                #up
                util(r - 1, c) if r > 0 and val < matrix[r - 1][c] else 0,
                #down
                util(r + 1, c) if r < R - 1 and val < matrix[r + 1][c] else 0,
                #left
                util(r, c - 1) if c > 0 and val < matrix[r][c - 1] else 0,
                #right
                util(r, c + 1) if c < C - 1 and val < matrix[r][c + 1] else 0,       
            ])      
        return max([util(r, c)
                   for r in range(len(matrix))
                   for c in range(len(matrix[r]))
                   ])
    
if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    s = Solution()
    print(s.longestIncreasingPath(matrix)) # 4