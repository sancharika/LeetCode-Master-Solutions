from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
use two heaps:
store max profit in maxheap (log n for pop)
store min capital in min heap
T- O(k.(logn +logn)) -> O(k. 2. logn)-> O(klogn)
S - O(n) (heap)

      """
        #initialize max profit
        maxProfit = [] #only projects that we can afford
        minCapital = [(c, p) for c, p in zip(capital, profits)] #min heap of tuplesbased on capital
        heapq.heapify(minCapital)
        for i in range(k):
            #while mincapital not empty and min capital c <= w
            while minCapital and minCapital[0][0] <= w:
                _, p = heapq.heappop(minCapital) #return c, p but only p needed not c
                #push cur p to max profit heap
                heapq.heappush(maxProfit, -p)
            #if no profit available break
            if not maxProfit: break
            #add max profit to w
            w += -heapq.heappop(maxProfit)
        return w
    

if __name__ == "__main__":
    s = Solution()
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    print(s.findMaximizedCapital(k, w, profits, capital)) #4