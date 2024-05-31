# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.head = None
    
    def linkedList(self, value):
        node = Node(value)
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
        nodes = []
        for i in range(len(list1)):
            self.linkedList(list1[i][0])
            nodes.append(self.head if i == 0 else nodes[-1].next)
        
        # Set the random pointers
        for i, (val, random_index) in enumerate(list1):
            if random_index is not None:
                nodes[i].random = nodes[random_index]
        
        return self.head
            
    
    def ans(self, list1):
        ll = self.listToLinkedList(list1)
        copied_head = self.copyRandomList(ll)

        # Create a list of nodes to handle the random pointer indices
        node_to_index = {}
        curr = copied_head
        index = 0
        while curr:
            node_to_index[curr] = index
            curr = curr.next
            index += 1

        # Generate the answer list with value and random pointer index
        curr = copied_head
        ans = []
        while curr:
            random_index = node_to_index.get(curr.random, None)
            ans.append([curr.val, random_index])
            curr = curr.next
        
        return ans
        
    
    def copyRandomList(self, head):
        #hashmap to store copy data
        oldToNew = {None:None}
        cur = head
        #to assign nodes
        while cur:
            
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        #to link nodes
        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew[curr.next]
            newNode.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]

        
        
if "__main__":
    s = Solution()
    head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    copyList = s.ans(head)
    print(copyList)