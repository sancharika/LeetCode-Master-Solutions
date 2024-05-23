class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
        
if "__main__":
    s = Solution()
    print(s.isPalindrome(121))