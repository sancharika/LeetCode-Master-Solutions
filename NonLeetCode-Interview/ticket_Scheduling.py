"""
Ticket Scheduling
----------------

You have `n` tickets, where the `i-th` ticket is dependent on the `j-th` ticket. This means that ticket `i` cannot be processed until ticket `j` has been processed. The dependencies are represented in a 2D array `dependencies` of size `n x n`, where `dependencies[i][j] = 1` indicates that ticket `i` depends on ticket `j`, and `dependencies[i][j] = 0` indicates no dependency.

Given this 2D array, your task is to determine all possible sequences of processing the tickets such that all dependencies are respected.

#### Example 1:

```
Input:
dependencies = [
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
]

Output:
[[0, 1, 2]]
```

Explanation:

Ticket     0 1 2
Ticket 0 | 0 1 0
Ticket 1 | 0 0 1
Ticket 2 | 1 0 0

   Ticket 0 
    ↙     ↖
Ticket 1 → Ticket 2

- Ticket 0 depends on Ticket 1.
- Ticket 1 depends on Ticket 2.
- Ticket 2 does not depend on any other ticket.

The only valid sequence to process the tickets is `[0, 1, 2]`.

#### Example 2:

```
Input:
dependencies = [
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 1, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0]
]

Output:
[[0, 1, 2, 3], [2, 4, 5, 6]]
```

Explanation:
0 → 1 → 7
↑   ↓
3 ← 2 → 4
    ↑   ↓
    6 ← 5

- Ticket 0 depends on Ticket 1.
- Ticket 1 depends on Ticket 7.
- Ticket 7 does not depend on any other ticket.
- Tickets 2, 3, 4, 5, and 6 have additional interdependencies as per the input.

The valid sequences to process the tickets are `[0, 1, 2, 3]` and `[2, 4, 5, 6]`.

#### Constraints:

- `1 <= n <= 1000`
- `dependencies[i][j]` is either `0` or `1`.
- No ticket will depend on itself, i.e., `dependencies[i][i] = 0`.

#### Task:
Write a function `findAllTicketSequences` that takes in a 2D array `dependencies` and returns a list of all possible sequences of processing the tickets such that all dependencies are respected.

"""
from typing import List
def findAllTicketSequences(tickets):
    n = len(tickets)
    dep_map = {i:[] for i in range(n)}
    # iterate to create the graph
    for i in range(n):
        for j in range(n):
            if tickets[i][j] == 1:
                dep_map[i].append(j)
    print(dep_map)    
    # take visited set and cycle and result
    visited = set()
    res = []
    cycle = []
    def dfs(ticket): 
        print(f"ticket {ticket}, cycle{cycle}")
        #if visited then cycle the add the cycle starting from the curr index in res
        if ticket in visited:
            print("value cyclic", ticket,visited)
            cycle_start = cycle.index(ticket)
            res.append(cycle[cycle_start:]) 
            return 
        #update visited set append cyclt tickets
        visited.add(ticket)
        cycle.append(ticket)
        # dfs for adjacent nodes
        for tickets in dep_map[ticket]:
            dfs(tickets)
        #remove visited and cycle last element to explore dfs
        visited.remove(ticket)
        cycle.pop()
        # remove node once visited to avaoid repeatations
        dep_map[ticket] = []

    # check for all tikects in case they are not connected        
    for ticket in dep_map:
        if ticket not in cycle:
            dfs(ticket)
    print(res)
    return res

            

tickets = [
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 1, 0, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0]
]
findAllTicketSequences(tickets)
# 0 → 1 → 7
# ↑   ↑   ↓
# 3 ← 2   4
#     ↑   ↓
#     6 ← 5
