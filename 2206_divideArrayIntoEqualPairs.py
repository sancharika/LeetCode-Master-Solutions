import collections
class Solution:
    def divideArray(self, nums):
        return all([v%2 ==0 for v in collections.Counter(nums).values()])
        
if "__main__":
    nums = [3,2,3,2,2,2]
    print(Solution().divideArray(nums))