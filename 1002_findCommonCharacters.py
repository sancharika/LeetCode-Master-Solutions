import collections
from functools import reduce
class Solution:
    def commonChars(self, words):
        #map -> creates a list of Counter objects, one for each word.
        #reduce-> a function cumulatively to the items of an iterable.
        # and_ (lambda x, y: x & y) -> (from operator) is applied between pairs of Counter objects.
        # and_ between two Counter objects computes the intersection, keeping only the minimum counts for each element
        return list(reduce(lambda x, y: x & y, map(collections.Counter, words)).elements())
if "__main__":
    s = Solution()
    words = ["bella","label","roller"]
    print(s.commonChars(words))