import numpy as np
class Solution:
    def findDuplicate(self, nums):
        # # T: O(n) S: O(n)
        # count = Counter(nums)
        # print(count)
        # for i,j in count.items():
        #     if j>1:
        #         return i

        #Required T: O(n) ans S: O(1)
        #Cyclic Linked List
        #floyd's algo
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            #where slow and slow1 meets -> strting point of cyclic Linked list
            if slow == slow1:
                return slow

if "__main__":
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))