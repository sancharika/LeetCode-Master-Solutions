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
    
    def detectCycle(self, head: ListNode) -> ListNode:
        # Initialize two pointers, slow and fast, to the head of the linked list.
        slow = head
        fast = head

        # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
        # until they either meet or the fast pointer reaches the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # If the fast pointer reaches the end of the list without meeting the slow pointer,
        # there is no cycle in the linked list. Return None.
        return None

# Testing the solution
if __name__ == "__main__":
    s = Solution()
    values = [3, 2, 0, -4]
    pos = 1  # Cycle starts at index 1 (node with value 2)

    # Create linked list and set up cycle
    head, nodes = s.listToLinkedList(values)
    s.createCycle(pos)

    # Detect cycle
    cycle_node = s.detectCycle(head)
    if cycle_node:
        print("Cycle starts at node with value:", cycle_node.val)
    else:
        print("No cycle detected.")
