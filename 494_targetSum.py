from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
DP with caching -  T- O(n.t) [n->len(nums), t->total sum[nums]]
caching with (index, total) 
recursive way-> sum of cur and diff of cur

        """
        #cahche - hashmap
        dp = {} #(index, total) - > no of ways possible

        def backtrack(idx, total):
            #base case reached end of array and already exist in cache
            if idx == len(nums): return 1 if total == target else 0
            if (idx, total) in dp: return dp[(idx,total)]

            dp[(idx, total)] = backtrack(idx+1, total + 
            nums[idx]) + backtrack(idx+1, total - nums[idx])

            print(dp, idx)
            return dp[(idx, total)]
        
        return backtrack(0,0)


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()
    print(s.findTargetSumWays(nums, target)) #5