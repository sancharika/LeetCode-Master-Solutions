class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
add unique element in hashset and while a element already in set then remove 
left element and add right element (move window)
        """
        charSet = set()
        l, res = 0, 0
        for r in range(len(s)):
            # if s[r] in hash set
            while s[r] in charSet:
                # remove left most element 
                charSet.remove(s[l])
                l+=1
            # add new char to hashset
            charSet.add(s[r])
            #max of sliding window length
            res = max(res, r - l+1)
        return res
if "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))