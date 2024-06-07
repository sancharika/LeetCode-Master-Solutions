class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            #below operations will be in order :
            # second pop to first pop
            elif c == "-":
                f, s = stack.pop(), stack.pop()
                stack.append(s - f)
            elif c == "/":
                f, s = stack.pop(), stack.pop()
                #to make it towards 0
                stack.append(int(s / f))
            else:
                #all the nums will be here so just append them in int format
                stack.append(int(c))
        return stack[-1]
if  __name__ == "__main__":
    tokens = ["10","6","+","9","-","3","*"]
    s = Solution()
    print(s.evalRPN(tokens)) # Output: 21