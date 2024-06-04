class Solution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = (start+end)//2
            #determine in whcih block it is
            if nums[mid] == target:
                return mid
            # start < mid [rotated]
            #left sorted portion
            if nums[start] <= nums[mid]:
                #if in mid < target < start
                #search right portion
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                #search left portion
                else:
                    end = mid - 1
                
            else:
                #go left -> end < target <mid 
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    # end >target> mid search right 
                    start = mid +1
        return -1
    
if "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], target=1))

        