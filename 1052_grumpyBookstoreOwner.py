from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        T -> O(n) S->O(1)
apply a fixed window of size `minutes`  
Slide a window of size minutes over the array, and for each window, calculate the maximum satisfaction that can 
be achieved by making the grumpy ones happy.
cur_total -> window all such that you can earn all points from `customers[i : i + minutes - 1]`, 
regardless of the value of grumpy.
satisfied -> windowPartial to denote the sum of the customers subarray [i : i + minutes - 1] where grumpy[i] equals 0
ans max of total - windowPartial + windowAll (total - satisfies + cur_total )
        """
        total = sum((1 - grumpy[i]) * customers[i] for i in range(len(customers))) # 0 if grumpy else sum
        all_window = 0
        partial_window = 0
        ans = 0
        for i in range(len(customers)):
            all_window += customers[i] #sum of cur customer
            partial_window += (1 - grumpy[i]) * customers[i] #sum based on grumpy or not
            #if fixed window size inc
            if i + 1 >= minutes:
                ans = max(ans, total - partial_window + all_window)
                l = i - minutes + 1 #update l 
                all_window -= customers[l] #remove prev element to maintain window
                partial_window -= (1 - grumpy[l]) * customers[l]
        return ans


"""
     0 1 2 3 4 5
 0 1 2 3 4 5 6 7
[1,0,1,2,1,1,7,5]
[0,1,0,1,0,1,0,1]
"""