from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
T- O(n*2^n)
dfs to find all subset
run dfs with including curr index num and with excluding it
[1,2,3]
           1           |         _  
    2              _   |      2      _
  [1,2]           [1]        [2]     []
3         _  | 3    _  |  3    _ | 3   _
[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []

or can use bit manipulation 
        """
        res = []
        sub = []

        def dfs(i):
            if i >= len(nums): #when reached here paased through leaf node
                res.append(sub.copy()) #subset wil get modify
                return 
            sub.append(nums[i]) #include nums
            dfs(i + 1) 
            sub.pop() #exclude nums
            dfs(i + 1)
        dfs(0)
        return res
    ## bit manipulation
        # l=[]
        # for i in range(1<<len(nums)):
        #     l.append([nums[j] for j in range(len(nums)) if(i&(1<<j))])
        # return l
if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3,4]))