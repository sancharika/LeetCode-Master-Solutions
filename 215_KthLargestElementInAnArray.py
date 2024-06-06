import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        #consider heap
        heap = []
        for num in nums:
            #push num in heap
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                #pop last element aka shortest element
        # nums [2,3,1,5,4] k=2
        '''
        heap = [2]-> [2,3]->[1,2,3] -> [2,3] ->[2,3,5] 
        -> [3,5] -> [3,4,5] -> [4,5] 
        '''

        return heap [0]


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums, k)) # output: 5