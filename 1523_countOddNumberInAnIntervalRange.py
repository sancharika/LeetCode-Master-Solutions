class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return int((high-low)/2)
            # for the rest of the cases it will be (high-low/2)+1
        else:
            return int((high-low)/2+1)

if "__main__":
    s = Solution()
    print(s.countOdds(3, 7))