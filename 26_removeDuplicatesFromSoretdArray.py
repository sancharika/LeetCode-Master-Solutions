class Solution:
    def removeDuplicates(self, nums):
        nums[:] =sorted(set(nums))
        return len(nums)

if "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(nums))