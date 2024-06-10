class Solution:
    def heightChecker(self, heights) -> int:
        exp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                count += 1
        return count
        
        #in one line
        # return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    print(Solution().heightChecker(heights)) # Output: 3