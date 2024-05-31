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
    
    def ans(self, list1):
        ll = self.listToLinkedList(list1)
        self.reorderList(ll)
        #reorder existing list
        curr = ll
        ans =[]
        while curr:
            ans.append(curr.val)
            curr = curr.next
        
        return ans


    def reorderList(self, head):
        if not head or not head.next:
            return
        #middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #revese second list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #merge first and second
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        
if __name__ == "__main__":
    s = Solution()
    nums = [2, 4, 5, 6]
    reordered = s.ans(nums)
    print(reordered)