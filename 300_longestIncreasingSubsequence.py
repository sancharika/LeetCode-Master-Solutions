from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
brute force-> DFS (choice to include or not include in subsequence)
-> T - O(2^N)
Optimal -> DFS with caching -> T - O(n^2)
lis = possible length of increseing sub sequence
eg: [1,2,4,3]
lis = [3,2,1,1]
can be O(nlogn) by using binary search and inserting in res
        """
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)

        """
        res = []      
        for n in nums:
            idx = bisect_left(res, n)
            if idx == len(res):
                res.append(n)
            else:
                res[idx] = n
        
        return len(res)
        """
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,8,101,18])) # 5