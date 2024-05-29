class Solution:
    def longestCommonPrefix(self, strs):
        mn, mx = min(strs), max(strs)
        print(mn, mx)
        for i in range(len(mn)):
            if mn[i] != mx[i]: return mn[:i]
             
        return mn

if "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))