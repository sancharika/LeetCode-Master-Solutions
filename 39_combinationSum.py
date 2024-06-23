from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
2^T (target value)
skip prev to avoid duplications

       """
        res = []
        # dfs(idx, curr-> list of added nums, total of cur)
        def dfs(i, cur, total):
            # print(cur)
            if total == target: 
                res.append(cur.copy())
                return
            # if idx out of bound of total greater than target
            if i >= len(nums) or total > target:
                return
            #inlcude nums[idx]
            cur.append(nums[i]) #cur idx to cur
            dfs(i, cur, total + nums[i])
            #exclude nums[idx]
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
    
if __name__ == "__main__":
    nums = [2,3,6,7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(nums, target)) # [[2,2,3],[7]]




        