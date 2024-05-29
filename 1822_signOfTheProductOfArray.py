import math
class Solution:
    def arraySign(self, nums):
        def signFunc(num):
            return 1 if num>0 else -1 if num<0 else 0
        product = math.prod(nums)
        return signFunc(product)

if "__main__":
    nums = [-1,-2,-3,-4,3,2,1]
    print(Solution().arraySign(nums))