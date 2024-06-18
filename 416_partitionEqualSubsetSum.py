from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        brute force - T-O(2^n)
        optimal - T - O(n*sum(nums)) DFS with cache <- S
        Dp cachingS- O(sum(nums))
bottom up
store possible element in set with sum of previous
trick -> sum(arr)%2 = sum of subset1 + sum of subset2
[1,5,11,5] -> 22 -> 11+ 11-> [11] [1,5,5]
set = {0, 5, 11, 16, 10,21,} [sum(curr_set + cur_num)]
      {1, 6, 12, 17    ,22} return if target exist else
       return false as never posible
        """
        if sum(nums)%2: return False
        dp = set()
        dp.add(0) #garantee 0 if not choose any nums
        target = sum(nums) // 2
        #revese but can do normal also
        for i in range(len(nums)-1, -1, -1):
            nextDP = set() #or clone dp basically needed to modify dp
            for t in dp:
                if (t + nums[i]) == target: return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            #reasign dp to nextdp
            dp = nextDP
        return True if target in dp else False
        

if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,5,11,5])) #True