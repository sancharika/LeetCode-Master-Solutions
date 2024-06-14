import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        use heap T- O(nlog n)
        """
        stones = [-s for s in stones] # for cfreating max heap -ve all 
        heapq.heapify(stones)
        while len(stones)> 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)# it will remain -ve
        stones.append(0) # is not stone add 0
        return abs(stones[0])



        """
        T ->  O(n ^ 2)
The outer while loop runs approximately O(n) times.
Each iteration of the while loop involves operations that take O(n) time.

        """
        # def remove():
        #     largest = stones.index(max(stones))
        #     return stones.pop(largest)
        
        # while len(stones) > 1:
        #     x = remove()
        #     y = remove()

        #     if x != y : stones.append(abs(y - x))
        # return stones[0] if stones else 0


if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1])) #1