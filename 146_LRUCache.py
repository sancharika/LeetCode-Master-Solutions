class ListNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        #create double linked list
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key-> Node not value
        #two pointers left and right
        #left => Least recent Use
        #right => Most recent Use
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        # left->right
        #     <-
        self.left.next, self.right.prev = self.right, self.left

    #dummy fucntion to remove node
    def remove( self, node):
        #remove node between left and right
        #prev <=> Node <=> next [remove node]
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #dummy function to insert node in right
    def insert(self, node):
        #prev <=> right
        #prev <=> Node <=> right
        prev, nxt = self.right.prev, self.right
        #prev-> Node <-nxt
        prev.next = nxt.prev = node
        #prev<-Node->nxt
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        #remove from linked list and add it to right 
        #keeping tagg or most recent used cache
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        # self.cache[key] stores node adderess
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #most recent cache update
            #by removing and inserting it to right
            self.remove(self.cache[key])
        #insert in hashmap -> address of node
        self.cache[key] = ListNode(key,value)
        #tab of most recent use
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #least rcent use left = 0,0 <=> LRU
            lru = self.left.next
            self.remove(lru)
            #delete from cache
            del self.cache[lru.key]

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    operations = ["LRUCache", "put", "get", "put", "put", "get", "get"]
    operands = [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]]
    output = []

    # Process each operation
    for i in range(len(operations)):
        if operations[i] == "LRUCache":
            lru = LRUCache(*operands[i])
            output.append("Null")
        elif operations[i] == "put":
            lru.put(*operands[i])
            output.append("Null")
        elif operations[i] == "get":
            result = lru.get(*operands[i])
            output.append(result)

    print(output)
