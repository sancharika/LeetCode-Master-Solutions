class Solution:
    def twoSum(self, nums, target):
        pair = {}

        for i, num in enumerate(nums):
            if target - num in pair:
                return [i,pair[target-num]]
            pair[num] = i

if "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))
        

        