from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T - O(amount * len(coins)) S- O(amount) [potential value for all amounts]
bottom up 
dp[sum] = min coin to get sum
        """
        dp = [amount + 1] * (amount + 1 ) # max amount
        dp[0] = 0 #base case

        #compute a from coins
        for a in range(1, amount + 1):
            for coin in coins:
                 if a - coin >= 0:
                    #possible combinations
                    dp[a] = min(dp[a], 1 + dp[a - coin]) #ex: coin = 4, a = 7 ==> dp[7] = 1 + dp[7-4]
        return dp[amount] if dp[amount] != amount + 1 else -1 #if default amount then no possible combinations

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 5)) #3