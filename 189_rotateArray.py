class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k - len(nums)
        i = len(nums) - k
        nums[:] = nums[i:] + nums[:i]
        print(nums)
        
if "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)

