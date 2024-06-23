from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    # function to convert list to linked list
    def list_to_linked_list(self, nums: List[int]) -> Optional[ListNode]:
        if not nums:
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
            return head
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
      T -O(n) S- O(n) [using in place linked list]
sub problem:
[1] [2] [5] [4]
[1,2] [4,5]
[1,2,4,5]
      """ 
        if not lists or len(lists) == 0:
            print(len(lists))
            return None
        #run loop whil only 1 linekin list exist
        while len(lists) > 1:
            #cur merged list
            mergedList = []
            #incrment by 2 steps
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None #i in bound
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else: 
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1: cur.next = l1
        if l2: cur.next = l2
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 5]
    l1 = solution.list_to_linked_list(nums)
    nums = [1, 3, 4]
    l2 = solution.list_to_linked_list(nums)
    nums = [2, 6]
    l3 = solution.list_to_linked_list(nums)
    lists = [l1, l2, l3]
    result = solution.mergeKLists(lists)
    while result:
        print(result.val)
        result = result.next
