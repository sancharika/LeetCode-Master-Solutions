from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = [] #current partition

        def dfs(i):
            if i >= len(s): 
                res.append(cur.copy())
                return 
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j + 1)
                    cur.pop()
        dfs(0)
        return res
    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True
        
if __name__ == "__main__":
    s = Solution()
    print(s.partition("aabb"))