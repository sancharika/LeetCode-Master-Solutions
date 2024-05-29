class Solution:
    def sortedSquares(self, nums):
        return sorted(map((lambda x:x*x), nums))
    
if "__main__":
    nums = [-4,-1,0,3,10]
    print(Solution().sortedSquares(nums))