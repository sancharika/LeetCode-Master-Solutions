from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        T - O(n) S-O(1)
Use 3 pointers -> left, mid, right
eg = [2,2,1,2,1] k =2
      l
      m
for r in range of nums: while valid window and m pointing to first odd:
    first res += l - m + 1
[2,2,1,2,1]
[2,1,2,1]
[1,2,1]


"""
        ans, odd, left, mid = 0, 0, 0, 0
        for r in range(len(nums)):
            #count odd
            if nums[r] % 2: odd += 1
            #check valid window
            while odd > k:
                #slide window
                if nums[left] % 2: odd -= 1
                # increment left and set mid to left
                left += 1
                mid = left
            if odd == k:
                #update mid to point at first odd
                while not nums[mid] %2:
                    mid += 1
                ans += (mid - left + 1)
        return ans
        
        


if __name__ == "__main__":
    nums = [2,2,1,2,1]
    k = 2
    print(Solution().numberOfSubarrays(nums, k)) # 4