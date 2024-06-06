# same as 846. Hand Of Straights
import collections
class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        # Time Complexity: 𝑂(𝑛log⁡𝑛) Space Complexity: 𝑂(𝑛)
        #size not divisible
        if len(nums) % k != 0 : return False
        #count hasmap with sorted key
        order = {k:v for k,v in sorted(collections.Counter(nums).items())}
        while order:
            # min of ordered count by next of iteretor
            minNum = next(iter(order))
            # iterate from min to k consecutive value
            for i in range(minNum, minNum + k):
                if i not in order: return False
                order[i] -= 1
                #remove empty elements
                if order[i]==0: order.pop(i)
        #if exits while then order has k element in consecutive way
        return True
    
if __name__ == "__main__":
    nums = [1,2,3,3,4,4,5,6]
    k = 3
    print(Solution().isPossibleDivide(nums, k)) # False [123] [345] [4_6]

        