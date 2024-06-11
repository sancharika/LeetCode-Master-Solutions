import collections
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = collections.Counter(arr1)
        res = []
        arr = sorted(arr1)
        for i in arr2:
            while i in count:
                res.append(i)
                count[i] -= 1
                arr.remove(i)
                if count[i]==0:
                    del count[i]
        
        res = res + arr
        print(res, count, arr)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.relativeSortArray([2,3,1,3,2,4,6
                               ,7,9,2,19], [2,1,4,3,9,
                                            6]))
    # Output: [2,2,2,1,4,3,3,9,6,7,19]
