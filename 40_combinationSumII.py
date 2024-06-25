from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
T - O(2^n) 
Trick : try to sort and check if prev num == cur num
        """
        res = []
    
        candidates.sort()
        # ([cur list], index, cur target[target - cur target])
        def backtrack(cur, idx, target):
            if target == 0:
                #found one possible combonation
                res.append(cur.copy())
                return
            #if cur target < 0 then cur list sums to greater than target
            if target <= 0: return

            prev = -1 
            for i in range(idx,len(candidates)):
                if candidates[i] == prev:
                    continue #to avoide duplication
                #include cur idx
                cur.append(candidates[i])
                # bacjtrack for remaining items
                backtrack(cur, i + 1, target - candidates[i])
                #exclude cur idx
                cur.pop()

                #update prev
                prev = candidates[i]
        backtrack([], 0, target)
        return res


            

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8)) # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]