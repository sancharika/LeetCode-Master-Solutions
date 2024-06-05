class Solution:
    def twoSum(self, nums, target: int):
        # Tîme - O(n) Space - O(1)
        #initiate two pointers
        l, r = 0, len(nums) - 1
        #run until l cross r
        while l < r:
            sum_target = nums[l] + nums[r]
            #if sum < target increment l
            if sum_target < target: l += 1
            ## if sum > target decrement r
            elif sum_target > target: r -= 1
            #sum == target
            # 1- indexed
            else: return [l+1,r+1]
        #if exits while loop then no index found
        return []
if "__main__": 
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target)) # Output: [1,2]