from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #T- O(nlogn) S - O(n)(for work storing difficulty and max profit)
        profits = 0
        total_profit = 0
        work = []
        for d, p  in sorted(zip(difficulty, profit)):
            profits = max(profits, p)
            work.append((d, max(profits, p))) #take max margin of profit
        def binarySearch(worker):
            left, right = 0, len(work)-1
            while left <=  right:
                mid = (left + right)//2
                if work[mid][0] > worker: right = mid - 1
                else: left = mid + 1 
            return right #right most return for max
        for w in worker:
            idx = binarySearch(w)
            if idx >= 0 and w>= work[idx][0]:
                total_profit += work[idx][1]
        return total_profit
        
if __name__ == "__main__":
    solution = Solution()
    difficulty = [4,2,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]
    print(solution.maxProfitAssignment(difficulty, profit, worker))