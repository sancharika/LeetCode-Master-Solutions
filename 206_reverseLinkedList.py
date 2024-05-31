# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        ll = ListNode()
        current = ll
        for val in head:
            current.next = ListNode(val)
            current = current.next
        # take prev, current -> head
        prev, curr = None, ll.next
        while curr:
            #temporay to store next node
            temp = curr.next
            #revese the link by pointing to prev
            curr.next = prev
            # prev -> curr
            prev = curr
            #curr -> temp
            curr = temp
        return prev
        
if "__main__":
    head = [1,2,3,4,5]
    reverse = Solution().reverseList(head)
    reverse_list = []
    while reverse:
        reverse_list.append(reverse.val)
        reverse = reverse.next
    print(reverse_list)