class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # # T- O(n^2) S-O(n)
        # # Initialize list of N friends, labeled from 1-N
        # circle = list(range(1, n + 1))

        # # Maintain the index of the friend to start the count on
        # start_index = 0

        # # Perform eliminations while there is more than 1 friend left
        # while len(circle) > 1:
        #     # Calculate the index of the friend to be removed
        #     removal_index = (start_index + k - 1) % len(circle)

        #     # Remove the friend at removal_index
        #     circle.pop(removal_index)

        #     # Update the start_index for the next round
        #     start_index = removal_index

        # return circle[0]
#---------------------------------------------------------------------
        # # T- O(n.k) S-O(n)
        # # Initialize deque with n friends
        # circle = deque(range(1, n + 1))

        # # Perform eliminations while more than 1 player remains
        # while len(circle) > 1:
        #     # Process the first k-1 friends without eliminating them
        #     for _ in range(k - 1):
        #         circle.append(circle.popleft())
        #     # Eliminate the k-th friend
        #     circle.popleft()

        # return circle[0]
        
#---------------------------------------------------------------------
        """
        The game involves repetitively eliminating the k-th friend from a circle, shrinking the size of the circle at every turn. This suggests that we can break down the problem into smaller, similar subproblems.

        1. The problem, initially dealing with a circle of n friends, now reduces to a subproblem with n-1 friends
        2. In the new subproblem, friend indices shift by -k. For instance, friend 3 moves from index 3 to index 1 in the new circle.

        We add k to f(n−1,k) to convert back to the original indexing of the circle of size n (we saw above how the new indexing on a circle of size n-1 shifts the original indexing by -k). Like before, we mod this value by the size of the circle to account for cases where the offset wraps around to the start of the circle.

        The base case is f(1,k)=0, as the last remaining friend will always be at index 0
        """
        # # T - O(n) S- O(1)
        # ans = 0
        # for i in range(2, n + 1):
        #     ans = (ans + k) % i
        # # add 1 to convert back to 1 indexing
        # return ans + 1
#---------------------------------------------------------------------

        #recursion
        if n == 1:
            return 1
        else:
            return (self.findTheWinner(n-1, k)+k-1) % n + 1


if __name__ =="__main__":
    s = Solution()
    print(s.findTheWinner(5, 3))