class Solution:
    def threeSum(self, nums):
        # T - O(n^2) S- O(n^2)
        # sort - O(nlogn)
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            #check i is not fisrt element and no duplicate values:
            if i > 0 and nums[i-1] == a:
                continue
            # two sum for remaining
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0: r -= 1
                elif three_sum < 0: l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1 #update only 1 pointer other will get updated based on sum
                    #ex [-2, -2, 0, 2, 2] l = 0, r = 2, if l++ (l[1] == previous one)
                    # so again l++ l = 3 sum = 2 then three_sum > 0 so r will update itself

                    #increse l until l< r and no duplicate values
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

if "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums)) 