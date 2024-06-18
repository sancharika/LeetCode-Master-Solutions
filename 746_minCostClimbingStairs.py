from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        T - O(n) S- O(1) (using array in place)
        bottom up aproach
        modify cost in place list (based on its last two elements)
        min of first 2 
        ex = [10, 15, 20] -> 
        [10,15,20,0] ->  [25, 15, 20, 0]
        so reverse loop for len(cost) - 3
        """

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            # add minimuim of 1 jump and 2 jump
            cost[i] += min(cost[i + 1], cost[i + 2])
        #return min of first 2
        print(cost)
        return min(cost[0], cost[1])
    
if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(Solution().minCostClimbingStairs(cost)) # 6