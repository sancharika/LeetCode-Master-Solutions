class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)
        return all(arr[i]-arr[i+1] == arr[0]-arr[1] for i in range(len(arr)-1) )

if "__main__":
    s = Solution()
    print(s.canMakeArithmeticProgression([3,5,1]))