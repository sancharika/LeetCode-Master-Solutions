def longestSubString(s: str):
    l,string_len = 0, 0
    hashmap = {}
    res = ""
    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
        while len(hashmap) > 2:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0: del hashmap[s[l]]
            l += 1
        if (r-l+1) > string_len: res = s[l:r+1]
        string_len = max(string_len, r - l + 1)
    return res

print(longestSubString("eceba"))