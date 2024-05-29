class Solution:
    def searchInsert(self, nums, target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left + (right - left)//2

            if nums[mid]==target:
                return mid

            elif target<nums[mid]:
                right = mid-1
            else:
                left=mid+1
            
        return left

if "__main__":
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))
