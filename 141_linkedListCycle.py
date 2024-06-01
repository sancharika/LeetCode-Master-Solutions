# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    
    def linkedList(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        # Find tail
        while current.next:
            current = current.next
        current.next = node
    
    def listToLinkedList(self, list1):
        self.head = None
        nodes = []
        for value in list1:
            self.linkedList(value)
            if self.head and len(nodes) == 0:
                nodes.append(self.head)
            else:
                nodes.append(nodes[-1].next)
        return self.head, nodes
    
    def createCycle(self, pos):
        if pos == -1:
            return
        cycle_start = None
        current = self.head
        index = 0
        while current.next:
            if index == pos:
                cycle_start = current
            current = current.next
            index += 1
        current.next = cycle_start

    def hasCycle(self, head):
        slow = fast = head
        #Floyd's Tortoise and Hare Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# Testing the solution
if __name__ == "__main__":
    s = Solution()
    values = [3, 2, 0, -4]
    pos = 1  # Cycle starts at index 1 (node with value 2)

    # Create linked list and set up cycle
    head, nodes = s.listToLinkedList(values)
    s.createCycle(pos)

    # Detect cycle
    cycle_node = s.hasCycle(head)
    print(cycle_node)