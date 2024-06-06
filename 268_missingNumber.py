class Solution:
    def missingNumber(self, nums) -> int:
        #by finding sum of n natural numbers
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        return expected_sum - sum(nums)

if __name__== "__main__":
    nums = [0, 1, 3]
    print(Solution().missingNumber(nums)) # Output: 2