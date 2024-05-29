class Solution:
    def removeElement(self, nums, val):
        count=nums.count(val)
        while count!=0:
            nums.remove(val)
            count=count-1
        return len(nums)
        
if "__main__":
    nums=[3,2,2,3]
    val=3
    print(Solution().removeElement(nums, val))
