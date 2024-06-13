from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
T- O(nlogn) for sorting S- O(n) due to the storage required for the sorted lists.
Find moves required to over come differnce of seats and students
        """
        seats = sorted(seats)
        students = sorted(students)
        return sum(abs(std - seat) for std, seat in zip(students, seats))
    
if __name__ == "__main__":
    seats = [3,1,5]
    students = [2,7,4]
    sol = Solution()
    print(sol.minMovesToSeat(seats, students)) # Output: 4

        