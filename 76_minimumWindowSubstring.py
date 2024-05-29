class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "" : return ""
        
        hashT, window = {}, {}
        # hash map for t
        for c in t:
            hashT[c] = 1 + hashT.get(c,0)
        
        have, need = 0, len(hashT)
        l = 0
        res, resLen = [-1,-1], float("inf")
        # window
        for r in range(len(s)):
            subS = s[r]
            window[subS] = 1 + window.get(s[r], 0) 
            # check sub string exist in T and ==
            if subS in hashT and window[subS] == hashT[subS]:
                #increase have
                have += 1
            while have == need:
                    #update current result
                    if (r-l+1)< resLen:
                        res = [l,r]
                        resLen = (r-l+1)
                    # remove 1st element and slide window
                    window[s[l]] -= 1
                    # s[l] in hashT and count of char is less (not exist anymore)
                    if s[l] in hashT and window[s[l]] < hashT[s[l]]:
                        have-=1
                    l+=1
        print(l,r,window)
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""

if "__main__":
     s = "ADOBECODEBANC"
     t = "ABC"
     print(Solution().minWindow(s,t))

        