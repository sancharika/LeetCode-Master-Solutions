class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} #tab of char count
        res = []
        # bucket sort T- klogn s- n
        """
        i= number of occurenace [numbers]
        ex [1,2,2,2,3,3,3,5] k=2
        {
            1: 1,
            2: 3,
            5: 2,
            3: 3
        }
        freq = [[],[1],[5],[2,3]]
        i number of occurance (starts from 0)
        freq[i] numbers having ith occurance
        """
        #i starts from 0 so nums +1
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for n,c in count.items():
            #ith -> number of occurance, i.e-> c
            freq[c].append(n)
        #check freq in revese
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                #add most occurance in res
                res.append(n)
                #if res lenght ==k we got answer
                if len(res) == k:
                    return res
        ### using Heap T - nlogn S-n
        # for i, c in count.items():
        #     heapq.heappush(res,(i,c))
        #     if len(res) > k:
        #         heapq.heappop(res)
        # return [i[-1] for i in res]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums,k)) # [1,2]
            
            
        
        
          