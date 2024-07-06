# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # T- O(n)  S- O(1)
        """
The current node: to iterate over the list
The previous node: to compare its value with the current node
Position of the current node: to calculate the distance in case it's a critical point
Position of the previous critical point: to calculate the distance from the next critical point
Position of the first critical point: to calculate the maximum distance
Minimum distance: to update the minimum distance for each pair of consecutive critical points
        """
        result = [-1, -1]

        # Initialize minimum distance to the maximum possible value
        min_distance = float("inf")

        # Pointers to track the previous node, current node, and indices
        cur = head.next
        prev = head
        nxt = head.next.next
        current_index = 1
        previous_critical_index = 0
        first_critical_index = 0
        while nxt:
            # Check if the current node is a local maxima or minima
            if (
                prev.val > cur.val and nxt.val > cur.val
            ) or (
                prev.val < cur.val and nxt.val < cur.val
                ):
                # If this is the first critical point found
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                else:
                    # Calculate the minimum distance between critical points
                    min_distance = min(
                        min_distance, current_index - previous_critical_index
                    )
                    previous_critical_index = current_index

            # Move to the next node and update indices
            current_index += 1
            cur = cur.next
            prev = prev.next
            nxt = nxt.next
        
        # If at least two critical points were found
        if min_distance != float("inf"):
            max_distance = previous_critical_index - first_critical_index
            result = [min_distance, max_distance]

        return result
        