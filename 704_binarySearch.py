class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+(right - left)//2
            if target == nums[mid]:
                return mid
            elif target< nums[mid]:
                right = mid-1
            else:
                left=mid+1
        return -1
    
if "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))
        