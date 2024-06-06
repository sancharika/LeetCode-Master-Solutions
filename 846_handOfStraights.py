# same as 1296. Divide Array in Sets of K Consecutive Numbers
import collections
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        # Time Complexity: 𝑂(𝑛log⁡𝑛) Space Complexity: 𝑂(𝑛)
        #size not divisible
        if len(hand) % groupSize !=0 : return False
        #count hasmap with sorted key
        count = collections.Counter(hand)
        orderedCount = {k: v for k, v in sorted(count.items())}
        while orderedCount:
            # min of ordered count
            minHand = next(iter(orderedCount))
            # iterate from min to groupsize consecutive value
            for card in range(minHand, minHand + groupSize):
                if card not in orderedCount: return False
                orderedCount[card] -= 1
                #remove empty elements
                if orderedCount[card] == 0: del orderedCount[card]
        #if exits while then orderedcount has groupsize element in consecutive way
        return True



if "__main__":
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], groupSize = 3))