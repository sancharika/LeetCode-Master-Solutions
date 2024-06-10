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
                #ex [4, 5, 6, 7, 1, 2, 3 ] mid =7 num = 2
                #we know num < mid we have two options 4, 5, 6 (left side) or 1, 2, 3
                #(right side) to know which side check if num > mid or num < start
                #if in mid < target < start
                
                if target > nums[mid] or target < nums[start]:
                    #if target is smaller then start then #search right portion
                    start = mid + 1
                #search left portion
                else: # target < nums[mid] or target > nums [start]
                    end = mid - 1
                
            else:
                #go left -> if num less than mid or num greater than end 
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else: #num greater tan mid or num less than end
                    # end >target> mid search right 
                    start = mid +1
        return -1
    
if "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], target=1))

        