class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if "__main__":
    s = Solution()
    print(s.strStr("sadbutsad","sad"))