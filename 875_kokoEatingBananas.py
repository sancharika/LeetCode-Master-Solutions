import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # k can be in range(0, max of piles)
        # min k when (sum of piles/k )<= h
        # mid - 1 -> right -> remove the right portion and add it to res
        # if left to mid has min k then res will be modified again and so on 
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left+right)//2
            ans = [math.ceil(pile/mid) for pile in piles]
            if sum(ans) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid +1
            
        return res

if "__main__":
    piles = [3,6,7,11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))