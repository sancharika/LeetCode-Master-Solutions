class Solution:
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

if "__main__":
    A = [3,1,2,4]
    print(Solution().sortArrayByParity(A))