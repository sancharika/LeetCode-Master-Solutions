from typing import List
class Solution:
    """
    use a separator to split and add length of words
    so that during decoding separate str until the length
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: res+= str(len(s)) + "#" +s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                #find length of word based on separtor
                j += 1
            length = int(s[i:j]) 
            print(f"{i}:{j} ",s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
    
if __name__=="__main__":
    s = Solution()
    strs = ["Hello", "World"]
    encoded = s.encode(strs)
    print(s.decode(encoded))  # ["Hello", "World"]

