"""
you have a stream of rpc requests coming in. Each log is of the form {id, timestamp, type(start/end)}. Given a timeout T, you need to figure out at the earliest possible time if a request has timed out.
Eg :
id - time - type
0 - 0 - Start
1 - 1 - Start
0 - 2 - End
2 - 6 - Start
1 - 7 - End
Timeout = 3
Ans : {1, 6} ( figured out id 1 had timed out at time 6 )
"""



def getTimeout(logs, timeout):
    """
    T- O(n) S-O(n) (hashmap and timeout dict)
use hashmap and two pointer
add start id in hashmap while valid pointer check prev request Timeout or not by the cur time

    """
    timeout_dict = {} # {id: timeout}
    id_map = {} # {id: timestamp}
    prev = 0
    for cur in range(len(logs)):
        cur_id , cur_timestamp, cur_status = logs[cur]
        print(cur_id , cur_timestamp, cur_status)
        #check if its timeout or not: prev id timestamp < cur_timestamp-timeout
        while prev < cur and logs[prev][1] <= cur_timestamp - timeout:
            prev_id, _, prev_status = logs[prev]
            #if prev start and in hashmap
            if prev_status == 'start' and prev_id in id_map:
                timeout_dict[prev_id] = cur_timestamp
                del id_map[prev_id]
            prev += 1
        
        if cur_status == "start":
            id_map[cur_id] = cur_timestamp
        else:
            #if cur_status == end remove from id_map
            if cur_id in id_map: del id_map[cur_id]
    return timeout_dict

"""
id 0 1   2 3     1
ti 0 1 2 3 4 5 6 7
out = 3

"""





logs = [(0, 0, 'start'), (1, 1, 'start'), (2, 3, 'end'), (3, 4, 'start'), (1, 7, 'end')]
timeout = 3
print(getTimeout(logs, timeout)) # {0: 3, 1: 4, 3: 7}