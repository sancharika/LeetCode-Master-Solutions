import collections
class Solution:
    def groupAnagrams(self, strs):
        # initiate dict
        ans = collections.defaultdict(list)
        for s in strs:
            # count of 0 length of 26
            count = [0]*26
            for c in s:
                # based on ascii increase the count of letters
                count[ord(c)-ord('a')] +=1
            ans[tuple(count)].append(s)
            """ans={
            (0,....,0) (len 26) = [collection of words with same char count]
            }
            {
                (1, .., 0, 1,.., 0): ['eat', 'tea', 'ate'], 
                (1, ..., 0, 1,., 0): ['tan', 'nat'], 
                (1, 1,.., 0, 1,., 0): ['bat']
            }
            """
        print(ans)
        return ans.values()

if "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs))