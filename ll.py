class linkedList:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode

class LL:
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, value):
        node = linkedList(value)
        if self.head is None:
            self.head = node
            return
        # insert tail
        currentNode = self.head
        while True:
            # if next none then its the tail
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next

        return self.head
    def print_ll(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def reverse_list(self):
        prev, curr = None, self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def middle_ll(self):
        slow =  fast = self.head
        slower = False
        while fast:
            print(fast.value, slow.value)
            fast = fast.next
            if slower:
                slow = slow.next
            slower = not slower
        return slow.value

l = LL()
node1 = l.insert(4)
node2 = l.insert("5")
node3 = l.insert(["list"])
l.print_ll()
# reverse = l.reverse_list()
# while reverse:
#     print(reverse.value)
#     reverse = reverse.next

middle = l.middle_ll()
print("Middle: ",middle)