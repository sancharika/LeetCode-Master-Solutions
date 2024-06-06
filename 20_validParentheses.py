class Solution:
    def isValid(self, s: str) -> bool:
        #hash map for closing
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = [] #using stack
        for c in s:
            #if closing parathesis and satck not empty:
            #closing one if in close to open [note thats why hasmap for closing]

            if c in closeToOpen:
                #if opening of is in tha last of stack
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else: #stack empty or not closing:opening
                    return False
            else: #c is opening we can have as many as we want if they have suitable closing
                stack.append(c)
        #true if stack empty
        return True if not stack else False

                

           
    
if "__main__":
    s = Solution()
    print(s.isValid("()"))