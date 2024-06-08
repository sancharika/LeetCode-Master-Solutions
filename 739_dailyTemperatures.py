class Solution:
    def dailyTemperatures(self, temperatures):
        """
create a stack that store tuple [temp, index]
pop it if the current temp is > and add index diff to result 
as stack will always be monotonically decreasing it might have 
same value elements sometime 

        """
        stack = []
        res = [0] * len(temperatures) #[temp, index]
        #search through the list
        for i,temp in enumerate(temperatures):
            #if stack then continue pop until temp < stack[temp]
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                #store index diff in index of res
                res[stack_index] = i - stack_index
            #add the curr temp & index in stack
            stack.append((temp,i))
        return res

# Time Complexity: O(n) where n is the number of temperatures
# Space Complexity: O(n) for the stack and result list
if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures)) # [1, 1, 4, 2, 1, 1, 0, 0]