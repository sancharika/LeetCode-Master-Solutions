# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def linkedListAppend(self,data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = node
    def listToLinkedList(self,list1):
        self.head = None #reinitaite
        for i in list1:
            self.linkedListAppend(i)
        return self.head
        

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        #while both true
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                #list2.value<list1.value
                tail.next = list2
                list2 = list2.next
            #regardless of list1 and list2 update tail
            tail = tail.next
        #if 1 list completes and other have some nodes remaining
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        #return linked list dummy : None->merged linked list
        return dummy.next
    
    def print_list(self, list1, list2):
        ll1 = self.listToLinkedList(list1)
        ll2 = self.listToLinkedList(list2)
        curr = self.mergeTwoLists(ll1, ll2)
        curr_list = []
        while curr:
            curr_list.append(curr.val)
            curr = curr.next
        
        return curr_list
    
if "__main__":
    s = Solution()
    list1 = [1,2,4]
    list2 = [1,3,5]
    merged_list = s.print_list(list1, list2)
    print(merged_list)




        