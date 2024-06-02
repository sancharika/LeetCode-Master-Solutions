class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums)-1
        curr_min = nums[0]
        while start <= end:
            #already sorted
            if nums[start] < nums[end]:
                curr_min = min(curr_min, nums[start])
                break

            mid = (start + end) //2
            curr_min = min(curr_min, nums[mid])
            #detemine if mid part of left rotated portion of right sorted portion
            if nums[mid] >= nums[start]:
                # if mid element greater then start min in right
                start = mid + 1
            else:
                #min in left
                end = mid - 1
        #edge case if rotation is n time and min in left most
        return curr_min
            
if "__main__":
    nums = [3,4,5,1,2]
    print(Solution().findMin(nums))