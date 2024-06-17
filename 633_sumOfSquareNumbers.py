from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        T-> O(sqrt(c)) S-> O(1)
0 <= a,b <= sqrt(c)  [a**2 <= c ] (consider 0 if c =0  the a, b=0)
a,b in range of [0, sqrt(c)]
Brute force: T-> O(sqrt(c)) <- S (for hashset)
create hashset for a**2 from [0, sqrt(c)]
then just find if two sums up to c

Optimal: search a, b like two sum 2
        """
        a, b = 0, int(sqrt(c))
        while a <= b :
            target = a * a + b * b
            if target < c:
                a += 1
            elif target > c:
                b -= 1
            else: return True
        return False
        
if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(5)) # True