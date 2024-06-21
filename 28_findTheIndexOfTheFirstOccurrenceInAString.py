class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        T->  O(n * m) in the worst case, O(n) on average. [n - haystack, m - needle]
        S -> O(1)
Boyer-Moore-Horspool algorithm skips sections of the haystack rather than checking every character, making it much 
faster in typical use cases.
        """
        return haystack.find(needle)

if "__main__":
    s = Solution()
    print(s.strStr("sadbutsad","sad"))