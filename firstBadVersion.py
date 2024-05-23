# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n-1
        left = 0
        while(left<=right):
            mid = left + (right-left)//2
            if isBadVersion(mid)==False:
                left = mid+1
            else:
                right = mid-1
        return left
    
if "__main__":
    s = Solution()
    print(s.firstBadVersion(5))
    
