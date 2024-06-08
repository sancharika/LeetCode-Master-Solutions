class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        """
        take a hashmap for remainder and its index.
        main idea is:
        ex [23, 2, 4, 6,7]
        23 % 6 = 5
        23 + 2 = 25 % 6 = 1
        25 + 4 = 29 % 6 = 5
        as 5 apears again it means we have a subarray divisible by k so find 
        the difference between index having same remainder 
        if >= 2 then gd subarray else continue the loop 
        T- O(n) S- O(n)
        """
        #initiate with -1 index so that if first element is divisible 
        # then return true as sub array size will be 1
        rem_map = {0 : -1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            rem = total % k
            # if rem doest exist add it
            if rem not in rem_map:
                rem_map[rem] = i
            #if rem exist check index diff
            elif i - rem_map[rem] > 1:
                #if subarray size  > 1 then found required subarray
                return True
        #exit loop then no gd sub array found
        return False
        
if __name__=="__main__":
    nums = [23,2,4,6,7]
    k = 6
    sol = Solution()
    print(sol.checkSubarraySum(nums,k)) #True