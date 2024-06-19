from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        brute force-> T - O(m^n) m-> coins(no of decisions) n-> amount (height)
        backtrack / dfs - T-O(m*n)
to avoid duplicates make sure never to use coins prev to the cur
eg: [1,2,5]
for 2 never use 1 same for 5 never use 2, 1
dp[amount] = [amount - cur coin]
        """
        dp = [0] *(amount + 1)
        dp[0] = 1
        for i in range(len(coins) -1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >=0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

if __name__ == "__main__":
    s = Solution()
    print(s.change(5, [1, 2, 5])) # 4

