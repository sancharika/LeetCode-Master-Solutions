"""
You have n items, cost is c(i) and delivery cost is d(i). If customer orders more than one item, then they get it 
for the minimum delivery cost. How do you find the maximum amount of money you can make after delivering m items? 

For e.g.
cost and delivery cost respectively (first column being cost, second being delivery cost):
Item 1: 7, 10
Item 2: 4, 15
Item3: 8, 1

m = 2

Input format (java): int n, int m, int[][] arr where n is the total number of items, m is the maximum number of items 
you can deliver, arr has each row with first element being cost, second being delivery cost.

Output: 31 (You choose the first two items because if you chose the 3rd item, the delivery cost for 2 items would be
1 + 1 (since 1 is the mimimum delivery cost) so you would end up with 23 + 2 = 25.
"""



import heapq
def solve(n, cost, delivery, m):
    """
Use priotity queue(min heap)
store sorted tuple(delivery, cost) in min heap if minheap>m pop smallest one
calulate max(min delivery * number of delivery + sum of cost)

Time Complexity: O(nlogn)
Space Complexity: O(n)
    """
    orders = sorted(zip(delivery, cost), reverse=True)

    pq = []
    minRate = float('inf')
    sumCost = 0
    res = 0
    for i in range(n):
        d, c = orders[i]
        heapq.heappush(pq, (d, c))
        minRate = min(minRate, d)
        sumCost += c
        if len(pq) > m:
            minRate, mc = heapq.heappop(pq)
            sumCost -= mc
        res = max(res, (minRate*len(pq)) + sumCost)
    print(res) # prints 31 with provided input


n = 3
cost = [7,4,100]
delivery = [10,15,1]
m = 2
solve(n, cost, delivery, m)