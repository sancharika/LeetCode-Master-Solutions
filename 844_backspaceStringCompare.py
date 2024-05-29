class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_char(st):
            stack =[]
            for char in st:
                if char == '#' and stack:
                    stack.pop()
                elif char!='#':
                    stack.append(char)
            return stack
        return remove_char(s)==remove_char(t)

if "__main__":
    s = Solution()
    print(s.backspaceCompare("ab#c","ad#c"))