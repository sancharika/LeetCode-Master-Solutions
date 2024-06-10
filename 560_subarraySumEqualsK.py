class Solution:
    def subarraySum(self, nums, k: int) -> int:
        """
Intution: take hashmap for prefix sum initiate hashmap with {0:1}, i.e 
sum i terms then find mod b/w it and k if it exist in hashmap increase count if not then add current sum and its count it works because it can have -ve numbers
ex: [4,5,0,-2,-3,1] k= 5
4-5 = -1     hashmap= {0:2, 4:2 ,9:2, 7:1, 5:1} res = 3
9-5 = 4
9-5 = 4
7-5 = 2
4-5 = -1
5-5 = 0
        """
        prefix_sum = {0: 1}
        curr = 0
        res = 0
        for n in nums:
            curr += n
            # find difference
            diff = curr - k
            #if diff in prefix sum
            res += prefix_sum.get(diff,0)
            print(res, diff)
            #add current sum
            prefix_sum[curr] = 1 + prefix_sum.get(curr,0)
        print(prefix_sum)
        return res
        
if __name__=='__main__':
    nums = [4,5,0,-2,-3,1]
    k = 5
    s = Solution()
    print(s.subarraySum(nums,k)) #3