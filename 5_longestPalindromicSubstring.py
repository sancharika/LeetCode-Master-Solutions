class Solution:
    """
check left and right string is equal or not from the current string
left and right starts from current string if odd else right strats from curr + 1
goes unil l-- and r++ meets the condition of l>=0 and r < len of string
keep track of window size update res if window size greater then previous one
    """
    def __init__(self):
        self.res, self.res_len = "", 0
        
    def validPalindrome(self, s, left, right):
         while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > self.res_len:
                    self.res = s[left:right+1]
                    self.res_len = right - left +1
                    #update left and right
                left -= 1
                right += 1
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s 
        for i in range(len(s)):
            #for counting odd palindrome length
            left, right = i, i
            self.validPalindrome(s,left,right)
           
            #for counting even palindrome length
            left, right = i, i+1
            self.validPalindrome(s,left,right)
            
        return self.res
        
if __name__ == "__main__":
     s = Solution()
     print(s.longestPalindrome("babad"))