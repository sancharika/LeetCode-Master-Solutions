class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {} #occurance tracking
        odd = 0 # odd count flag
        for n in range(len(s)):
            hashmap[s[n]] = 1 + hashmap.get(s[n], 0)
            # if n count odd flag increment else dercement
            if hashmap[s[n]] % 2 == 0:
                print(odd)
                odd -= 1
            else:
                odd += 1
        print(hashmap, odd)
        # If an odd frequency character is found, increment the length by 1 to 
        # account for placing one odd character in the center of the palindrome.
        if odd > 1:
            return len(s) - odd + 1
        # if not odd occurance
        return len(s)
        
if "__main__":
    s = "abccccdd"
    palindrome = Solution().longestPalindrome(s)
    print(palindrome)
        