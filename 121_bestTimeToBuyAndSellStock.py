class Solution:
    def maxProfit(self, prices):
        left, right =0, 1 #left-> buy, right-> sell
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        return maxP

if "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))