from typing import List
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        T- O(n) S- O(3) -> O(1)
        count number of occruance update nums in place positions and del from count
        """
        idx = 0
        count = Counter(nums)
        for color in range(3):
            while count[color]:
                nums[idx] = color
                idx += 1
                count[color] -= 1
                if not count[color]: 
                    del count[color]
        print(nums)

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)