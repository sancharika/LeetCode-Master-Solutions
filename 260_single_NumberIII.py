import collections
class Solution:
    def singleNumber(self, nums):
        #hashmap for count
        # count = collections.Counter(nums)
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        return [i for i in count if count[i]==1]

if "__main__":
    s = Solution()
    nums= [1,2,1,3,2,5]
    single_number = s.singleNumber(nums)
    print(single_number)
