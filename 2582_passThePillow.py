class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # # T - O(time) S- O(1)
        # current_pillow_position = 1
        # current_time = 0
        # direction = 1
        # while current_time < time:
        #     if 0 < current_pillow_position + direction <= n:
        #         current_pillow_position += direction
        #         current_time += 1
        #     else:
        #         # Reverse the direction if the next position is out of bounds
        #         direction *= -1
        # return current_pillow_position

        # T- O(1) S - O(1)
        # Calculate the number of complete rounds of pillow passing
        full_rounds = time // (n - 1)

        # Calculate the remaining time after complete rounds
        extra_time = time % (n - 1)

        # Determine the position of the person holding the pillow
        # If full_rounds is even, the pillow is moving forward.
        # If full_rounds is odd, the pillow is moving backward.
        if full_rounds % 2 == 0:
            return extra_time + 1  # Position when moving forward
        else:
            return n - extra_time  # Position when moving backward

if __name__ == "__main__":
    s = Solution()
    print(s.passThePillow(3, 5))