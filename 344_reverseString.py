class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        ## 1
        s[:] = s[::-1]
        return s

        ##2
        # s.reverse()

if "__main__":
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
        