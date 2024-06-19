class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
Bottom up - O(text1*text2)
based on comapring text1[i] and text2[i] we can break i into sub problems
eg:
abcde ace -> a common to sub problem-> bcde ce
bbcde ace -> 1th term not common sub problem-> bcde ace | bcde ce
so 2D decision problem 
if two matches go diagonally if not then either right or down
if diagonal -> 1 ++ else 0++
dp[i][j] = max(down, right )
diagonal -> [i + 1] [j + 1]
        """
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        #matirx in reverse
        for i in range(len(text1)-1, -1, -1): 
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] #diagonal add 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) #not match then max of down or right
        return dp[0][0] #bootm up so [0][0] is the lcs


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace")) #3