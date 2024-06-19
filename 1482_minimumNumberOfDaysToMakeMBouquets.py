from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        T - O(nlog(max(n))) [binary search range from day 1 to max(n)]
        S- O(1)
binary search the day then create array if bloomday<=day
search if array based on cur day has required consecutive k days
if day found search if day less then cur day possible by searching left portion
        """
        if m*k > len(bloomDay): return -1

        def bloom(day):
            length, bouquet = 0, 0
            for bloom in bloomDay:
                if bloom <= day:
                    length += 1 #find consecutive length
                    if length >= k:
                        length = 0 #re initiate 
                        bouquet += 1 #possible bouquet
                else: length = 0
            return bouquet >= m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l+r) // 2
            if bloom(mid): r = mid
            else: l = mid + 1
        return l #min day will be in left pointer
    

if __name__ == "__main__":
    bloomDay = [1,10,3,10,3]
    m = 3
    k = 1
    print(Solution().minDays(bloomDay, m, k)) #3


        