from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
T - O(n) S-O(1)
at each step we need to take care about cur. maximum.
# If it's higher than the previous one, increment count of steps as
# max - min, otherwise continue to move forward.
        """
        res = 0
        cur = 0
        for x in target:
            if x > cur:
                res += (x - cur)
                print(x, cur, res)
            cur = x
        return res
    
if __name__ == "__main__":
    target = [1,2,3,2,1]
    s = Solution()
    print(s.minNumberOperations(target)) # 3