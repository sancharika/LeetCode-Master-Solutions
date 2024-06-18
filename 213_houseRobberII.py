from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        T- O(n) S-O(1)
reuse house rob1 with eliminatinge first and last 
simultanously as they are in circle 
take -> nums[1:] and nums[:-1]
ex -> [2,9,8,3,6]
[9, 8, 3, 6]
[2, 9, 8, 3]
        """
        # edge case where nums len== 1so max of nums[0] also
        #as nums[1:] [:-1] will be empty for len(nums)==1
        return max(nums[0], self.robHouse(nums[1:]), self.robHouse(nums[:-1]))

    def robHouse(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2
    

if __name__ =="__main__":
    s = Solution()
    print(s.rob([2,3,2])) #3