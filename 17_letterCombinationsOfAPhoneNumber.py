from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
T - O(n*4^n) [7, 9 has 4 char || n-> len(digits)]
        """
        res = []
        #digit maps
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        #idx of digits and cur string created
        def backtrack(idx, curStr):
            if len(curStr) == len(digits):
                #every char mapped
                res.append(curStr)
                return
            
            for c in digitToChar[digits[idx]]:
                #every char in map
                backtrack(idx + 1, curStr + c) # add cur c to curStr
        #edge case digits [""]
        if digits:
            backtrack(0, "")
        return res
        

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("79"))