from typing import List
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        """
T - O(m*n) S-O(m*n) [because of stroing m x n data in 1D]
matrix -> m x n take top bottom, left right.
until top <= bottom and left <=  right
itereatre through 
top -> left to right => top ++
right -> top to bottom => right --
chck top <= bottom -- bottom -> right to left in reverse => bottom --
chck left <= right -- left -> bottom to top in reverse => left ++
        """
        m = len(mat)
        n = len(mat[0])
        top ,  bottom =0, m-1
        left, right = 0, n - 1
        path = []
        while top <= bottom and left <= right:
            #for top
            for i in range(left, right+1):
                path.append(mat[top][i]) 
            top += 1
            # for right most top to bottom
            for i in range(top, bottom+1):
                path.append(mat[i][right])
            right -= 1
            #for bottom in revese
            if top <= bottom:
                for i in range(right, left-1, -1):
                    path.append(mat[bottom][i])
                bottom -= 1
            # for left most bottom to top
            if left <= right:
                for i in range(bottom, top-1,-1):
                    path.append(mat[i][left])
                left += 1
        
        return path
            
if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.spiralOrder(mat)) # [1, 2, 3, 6, 9, 8, 7, 4, 5]