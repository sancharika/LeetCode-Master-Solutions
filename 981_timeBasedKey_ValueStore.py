class TimeMap:
    """
hashmap = {
    key: [value, timestamp]
}
binary search time stamp if timestamp >= mid return mid
as timestamp can be equal or not exist if not exist return nearest

    """
    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap.get(key,[]) #if not present 
        low, high = 0, len(values) -1
        res = "" #if not there
        while low <= high:
            mid = (low + high)//2
            if timestamp >= values[mid][-1]:
                res = values[mid][0]
                low = mid + 1
            else:
                high = mid -1
        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
if "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    obj.set("foo", "bar2", 4)
    obj.set("foo", "bar3", 7)
    print(obj.get("foo", 2))
    