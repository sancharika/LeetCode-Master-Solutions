class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hash map for count
        count = {}
        #maxF for max cnharcter
        res, l, maxF = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # max occurnace of the window
            maxF = max(maxF, count[s[r]])
            # number of character to change is greater than operation
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

if "__main__":
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))