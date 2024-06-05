class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## T- O(n) S- O(n)
        # s = ''.join(i for i in s if i.isalnum()).lower()
        # return s == s[::-1]

        ## T- O(n) S - O(1) [using 2 pointer]
        
        l, r = 0, len(s) -1
        #stops whne l pass r
        while l < r:
            # to avoid l go out of bound
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r-1
        return True

    def isValid(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )

if "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))