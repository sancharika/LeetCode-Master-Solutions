class Solution:
    def climbStairs(self, n: int) -> int:
        """
brute force: T - O(2^n) 
optimal - >T - O(n) s- O(1)
dfs decision tree from 0 to 1, 2| 1 to 1, 2 | 2 to 1, 2 and so on
repited tree from 2 to n-1
to avoid repeted storing use memoization
stair: 0 1 2 3 4 5
       8 5 3 2 1 1 
how many step it takes -> fibbonaci sereis 
consider two pointer for last two values
keep sliding two pointer n-1 time with 1 having sum of curr two
and swaping second pointer with first
        """
        one, two = 1, 1
        for _ in range(n-1):
            one, two = one + two, one
        return one
        

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(10)) # 89