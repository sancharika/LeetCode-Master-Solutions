

class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        # Calculate the time each car will take to reach the target
        #reverse and sort position to avoid min position not tracking
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        fleets = 0
        while times:
            lead_time = times.pop(0)  # the time for the car in the lead
            fleets += 1  # this car starts a new fleet
            # Remove all cars that are caught by the current fleet
            while times and times[0] <= lead_time:
                times.pop(0)
        
        return fleets

if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(12, [10,8,0,5,3],
                            [2,4,1,1,3]))