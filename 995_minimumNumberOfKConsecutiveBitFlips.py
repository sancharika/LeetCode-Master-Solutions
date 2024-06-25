from typing import List
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        T -> O(n)  S -> O(k) (queue size)
start window -> 0, k
flip entire window ==> 0 -> 1 | 1 -> 0
next window again where its 0
keep track of operations made -> cur window + len(queue)
identify where to flip if no of operations % 2 == 0
when flipped add idx to queue
popleft queue when idx doesnt effect last filp -> by checking idx > queue[0] - k + 1 (last flipped window)
case: if cur window exceeds, i.e cur idx + k > len of nums --> no possible flips return -1

        Better -> S- O(1) (changing in place values instead of maintaing queue)

by taking a varaible flip -> instead of append increment flip and change nums[i] = 2 (for knowing its flipped)
i-k >=0 -> then cur valid window passed
so instead of popleft decrment flip

        """
        # q = deque()
        # res = 0 

        # for i in range(len(nums)):

        #     while q and i > q[0] - k + 1:
        #         q.popleft()
        #     # how many operations are made
        #     if (nums[i] + len(q)) %2 ==0:
        #         #if not valid window remaining
        #         if i + k > len(nums): return -1
        #         res += 1
        #         q.append(i)
        # return res

        ## S- O(1)
        flip, res = 0, 0

        for i in range(len(nums)):

            if (i-k) >= 0 and nums[i - k] == 2:
                flip -= 1
            # how many operations are made
            if (nums[i] + flip) %2 ==0:
                #if not valid window remaining
                if i + k > len(nums): return -1
                res += 1
                flip += 1
                nums[i] = 2
        return res

        