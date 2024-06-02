class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        low, high = 0 , cols-1
        while top <= bottom:
            curr_row = (top+bottom)//2
            # > than last element of the row
            if target > matrix[curr_row][-1]:
                top = curr_row+1
            elif target < matrix[curr_row][0]:
                bottom = curr_row -1
            else:
                break
        # exit loop when top > bottom so no row has element
        if not (top <= bottom):
            return False
        row = (top + bottom)//2
        while low <= high:
            mid = (low+high)//2
            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid -1
            else:
                return True
        return False

if "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[
        23,30,34,60], [100,101,102,120]]
    target = 3
    print(Solution().searchMatrix(matrix, target))