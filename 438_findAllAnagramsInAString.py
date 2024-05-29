class Solution:
    def findAnagrams(self, s: str, p: str):
        # anagram length greater then string then its impossible to have anagram in s
        if len(p) > len(s): return []
        countS, countP = {}, {}
        for c in range(len(p)):
            countP[p[c]] = 1 + countP.get(p[c], 0)
            countS[s[c]] = 1 + countS.get(s[c],0)
        l = 0
        # index from 0 as already compared s and p string
        res = [0] if countP == countS else []
        # comparison for s string don till length of p
        for r in range(len(p),len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            countS[s[l]] -= 1
            # pop keys with 0 value for equality 
            if countS[s[l]] == 0:
                countS.pop(s[l])
            l += 1
            # if same append left pointer index
            if countS==countP:
                res.append(l)
        return res

if "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))