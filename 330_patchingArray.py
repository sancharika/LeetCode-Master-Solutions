from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
check sum till cur <= num[cur] if yes add sum else add cur
Check if the current number in the list (nums[i]) can be used to form miss. If yes, add it to miss to extend the range of formable sums and increment the index i.
If nums[i] is greater than miss or all numbers are already used, add miss itself to cover the smallest unformable sum, and double the value of miss.
        """
        patch, idx = 0, 0
        sum_patch = 1

        while sum_patch <= n:
            if  idx < len(nums) and nums[idx] <= sum_patch:
                sum_patch += nums[idx]
                idx += 1
            else: 
                sum_patch += sum_patch
                patch += 1
            print(sum_patch, patch)
            
        return patch


if __name__=="__main__":
    nums = [1, 3]
    n = 9
    print(Solution().minPatches(nums, n)) # Output: 2