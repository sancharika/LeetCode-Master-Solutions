class Solution:
    def productExceptSelf(self, nums):
        # consider res with 1 of length nums
        res = [1] * len(nums)
        # postfix, prefix to 1
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            # res will have prefix
            res[i] = prefix
            prefix *= nums[i]
        # in revese order mul postfix of res till 0 i.e -1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums)) # [24,12,8,6]