class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##### Solutuion 1
        #in fot same lenght not anagram
        if len(s) != len(t):
            return False
        #hashmap
        cs , ct = {}, {}
        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i],0)
            ct[t[i]] = 1 + ct.get(t[i],0)
        #anagram will have same hashmap
        return cs == ct
    
        #### Solution 2
        # return Counter(s) == Counter(t)

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))