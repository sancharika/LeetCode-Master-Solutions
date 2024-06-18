from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # T- 2^n
        #works if nums is unique
        res = []

        # base case
        if len(nums) == 1: return [nums[:]]

        for _ in range(len(nums)):
            #pop first element
            n = nums.pop(0)
            perms = self.permute(nums)
            # ex nums [1, 2, 3]-> [2, 3], [3, 2] -> [2,3,1],[3,2,1]
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n) #add n back in last 

        return res
        
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))