from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        T- O(nlogn) S- O(1)
        sort the array
        keep track of curr max and how much increment require to get tracked number
        keep increasing the tracker for required max
        """
        nums.sort()
        tracker = 0
        increment = 0
        for num in nums:
            tracker = max(tracker, num)
            increment += tracker - num
            tracker += 1
        return increment
    
if __name__ == "__main__":
    nums = [3,2,1,1,2,7]
    print(Solution().minIncrementForUnique(nums)) # 6
        