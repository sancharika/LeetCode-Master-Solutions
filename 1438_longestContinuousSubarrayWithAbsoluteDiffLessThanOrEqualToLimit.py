from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
brute force -> O(n^2) for subarray * O(n) max abs diff
Optimal -> T -> O(n) S - O(n) [foe deque]
use sliding window -> coz continuos sub array
keep track of max abs diff 
move right -> inc max abs diff
move left -> dec max abs diff
two dequeues (maxq and minq) to store the max and min in the cur window.
if max - min > limit --> slide win by removing max n min until within limits

        """
        maxq = deque()
        minq = deque()
        res, left = 0, 0
        for r in range(len(nums)):
            #update min and max for cur window
            # Maintain the decreasing order in maxq
            while maxq and nums[r] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[r])
            while minq and nums[r] < minq[-1]:
                minq.pop()
            minq.append(nums[r])
            
            if maxq[0] - minq[0] > limit:
                #slide window
                if nums[left] == maxq[0]:
                    maxq.popleft()
                if nums[left] == minq[0]:
                    minq.popleft()
                left += 1
            res = max(res, r - left + 1) #update max window

        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([8,2,4,7], 4)) #