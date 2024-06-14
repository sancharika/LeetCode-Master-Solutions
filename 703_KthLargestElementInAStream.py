from typing import List
import heapq
class KthLargest:
    #Min head of size k add/ pop -> logn || min -> O(1)
    # only have to store k largest value 
    #worsr case nlogn because add + pop (n - k)log n if k << then
    #nlogn
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        print(self.minHeap)
        return self.minHeap[0]
        
if __name__ == "__main__":
    nums = [4, 5, 8, 2]
    k = 3
    obj = KthLargest(k, nums)
    print(obj.add(3)) # returns 4
    print(obj.add(5)) # returns 5
    print(obj.add(10)) # returns 5
    print(obj.add(9)) # returns 8
    print(obj.add(4)) # returns 8   
    
