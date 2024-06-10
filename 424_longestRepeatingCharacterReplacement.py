class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hash map for count
        count = {}
        #max frequency for max character count
        res, l, maxF = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # max occurnace of the character
            maxF = max(maxF, count[s[r]])
            # if the window size is more than max occurance
            # number of character to change is greater than operation
            #[maxF can be max(count.values())]
            while (r - l + 1) - maxF > k:
                #slide the window by decreasing the count of s[l] and l+=1
                count[s[l]] -= 1
                l += 1
            #store max window len
            res = max(res, r - l + 1)
        return res

if "__main__":
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))