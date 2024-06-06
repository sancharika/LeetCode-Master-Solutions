class Solution:
    def longestConsecutive(self, nums):
        # solve it by checking previous neighbour existance
        #initiate a set
        num_set = set(nums)
        longest = 0
        for n in num_set:
            #check prev element present in set to avoid repetition:
            #if not iniitiate l = 1
            if (n-1) not in num_set:
                length = 1
                #if consecutive
                while (n+length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
if __name__=="__main__":
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))