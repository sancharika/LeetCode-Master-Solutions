class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        backtracking to have n open ( and close only when < open
        if open == close == n: we found all combination
        ex: n = 2
        (
    ()      ((
()(            (()
()()             (())
ans = ["()()","(())"]

pop to backtrack the changes made to the stack 
during the recursive exploration of different 
combinations of parentheses. It ensures that the 
stack is restored to its previous state before 
exploring other possibilities.
        """
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        #start with 0,0
        backtrack(0, 0 )
        return res


if __name__=="__main__":
    s = Solution()
    print(s.generateParenthesis(2)) #["()()","(())"]