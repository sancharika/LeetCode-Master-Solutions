class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        """
Intution: take hashmap for prefix sum initiate hashmap with {0:1}, i.e 
sum i terms then find mod b/w it and k if it exist in hashmap increase count if not then add current sum and its count
ex: [4,5,0,-2,-3,1] k= 5
4%5=4           hashmap={0:2, 4:2, 2:1}
9%5=4
9%5=4
7%5=2
4%5=4
5%5=0
        """
        prefix_mod = {0:1}
        res = 0
        current = 0
        for n in nums:
            #current Sum
            current += n
            mod = current % k
            #if mod in prefix_mod
            res += prefix_mod.get(mod, 0)
            prefix_mod[mod] = 1 + prefix_mod.get(mod, 0)
        print(prefix_mod)
        return res
    
if __name__ == "__main__":
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(Solution().subarraysDivByK(nums, k)) # 7
        