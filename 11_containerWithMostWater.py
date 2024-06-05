class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) -1
        res = 0
        while l < r:
            res = max(res, (r-l)*min(height[l],height[r]))
            # if l is less than r l++
            if height[l] < height[r]:
                l += 1
            #if l> r and also if l==r(if l == r then wheter l++ or r--)
            else:
                r -= 1
        return res

if "__main__":
    nums = [1,8,6,2,5,4,8,3]
    print(Solution().maxArea(nums)) #49