class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]

if "__main__":
    nums = [0,2,1,5,3,4]
    print(Solution().buildArray(nums))