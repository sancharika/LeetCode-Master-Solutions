from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        0         1
       2 3  4    3 4
      4     2   
     16  5  16  12  15 
optimal->sub problem -> find max of sub array from the entire array
rob = max(arr[0] + rob(arr[2:]), rob(arr[1:n])) 
max from arr[0] and sub problem and with arr skiping arr[0] 
need only two max that we can rob from
     """
        rob1, rob2 = 0, 0 #rob1-> the 1st house rob2 -> 2nd house

        for n in nums:
            #[rob1, rob2, n, n+1,...]
            temp = max(n + rob1, rob2)
            rob1 = rob2 #shift both to 1
            rob2 = temp

        #rob2 will be at last 
        return rob2


if __name__ == "__main__":
    nums = [2,7,9,3,1]
    print(Solution().rob(nums)) #12