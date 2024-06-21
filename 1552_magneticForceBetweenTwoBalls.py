from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        T - O(n log n + n log (max(position) - min(position)))
        S - O(1)
binary search: Is it feasible to position `m` balls such that the minimum distance between any two distinct balls is at least `x`?
l, r= 1, the difference between the maximum and minimum positions
if f(mid) is true, we can shift l to the right to potentially find a greater distance that still satisfies the condition. Otherwise, if f(mid) is false, we need to shift r to the left as we need to decrease the distance.
        """
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            last_pos, balls = position[0], 1
            for i in range(1, len(position)):
                #curr pos - last pos >= mid last = cur pos ball++
                if position[i] - last_pos >= mid:
                    last_pos = position[i]
                    balls += 1
            
            if balls >= m:
                ans = mid #possible answer
                l = mid + 1 #to find larger l
            else: r = mid - 1
        return ans