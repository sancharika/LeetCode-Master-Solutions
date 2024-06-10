# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1, l2):
        """
take dummy linked list add teo list val or 0 if list val none then take carry 
curr node .next(curr val) will create node for next one
then update all linked list to next one
        """
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry =val //10
            val = val % 10
            print(val)
            curr.next = ListNode(val)
            # for carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next
    
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
    
    def ans(self, list1, list2):
        ll1 = self.listToLinkedList(list1)
        ll2 = self.listToLinkedList(list2)
        curr = self.addTwoNumbers(ll1, ll2)
        ans =[]
        while curr:
            ans.append(curr.val)
            curr = curr.next
        
        return ans
    
    
    

if "__main__":
    list1 = [2,4,3]
    list2 = [5,6,4]
    print(Solution().ans(list1, list2))