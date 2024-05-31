# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def linkedList(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        #find tail
        while current.next:
            current = current.next
        current.next = node
    
    def listToLinkedList(self, list1):
        self.head = None
        for i in list1:
            self.linkedList(i)
        return self.head
    
    def ans(self, list1,n):
        ll = self.listToLinkedList(list1)
        self.removeNthFromEnd(ll, n)
        #reorder existing list
        curr = ll
        ans =[]
        while curr:
            ans.append(curr.val)
            curr = curr.next
        
        return ans
    
    def removeNthFromEnd(self, head, n: int):
        #two pointer -> left and right always have difference of n
        dummy = ListNode(0,head)
        #0-> head-> so on
        #left -> head right-> head+n
        left = dummy
        right = head
        # shift right by n
        while n>0:
            right = right.next
            n -= 1
        
        #until right is not null shift left and right by 1:
        while right:
            left = left.next
            right = right.next

        #when right == null left will always at where we want 
        left.next = left.next.next #skip 1 node

        return dummy.next
        
if "__main__":
    s = Solution()
    nums = [1,2,3,4,5]
    n = 2
    remove = s.ans(nums,n)
    print(remove)

