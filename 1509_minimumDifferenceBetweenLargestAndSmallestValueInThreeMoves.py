from typing import List
import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        T - O(nlogn) [for sorting]
sort the arr
then use two pointer to remove 3 elements each time and abs diff of cur window
optimisation-> T- O(n)
only min 4 [0,1,2,3] and max 4 [3,2,1,0] is needed in b/w nums not needed to calculate
can do it by heapify (t - O(n))
to search min and max 4 - t - O(4logn)
        """

        if len(nums) < 5: return 0 
        res = float("inf")

        # # T - O(nlogn)
        # nums.sort()
        # #4 options remove 3, 2, 1, 0 from first
        # for l in range(4):
        #     r = len(nums) - 4 + l #to shift +1 every time
        #     #abs diff
        #     res = min(res,abs(nums[r] - nums[l]))
        # return res

        # T - O(n) [O(nlog4) - >O(2n)]
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))
        for i in range(4):
            res = min(res, max_four[i]-min_four[i])
        return res


if __name__=="__main__":
    s = Solution()
    print(s.minDifference([1,5,0,10,14]))