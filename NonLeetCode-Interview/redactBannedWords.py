"""
given two files find words that exist in both redact and banned words replace them with _REDACTED_
 - Example input 'redact_me.txt':

I DO NOT LIKE green eggs and ham

Not in a box not with a fox
Not in a house not with a mouse

 - Example input banned_words.txt:

fox
egg
toybox
not



Example 'redacted' output:

I DO _REDACTED_ LIKE green eggs and ham

_REDACTED_ in a box _REDACTED_ with a _REDACTED_
_REDACTED_ in a house _REDACTED_ with a mouse

------------------------------------------------------------------

input - > 2 files 1. redact_me.txt
2. banned_words.txt
output: redact_me.txt -> banned words will be replaced

no duplicates
redact_me can be larger file

redeact = read "redact_me.txt"
total_length = len(redact)

* conditions*
total_length > 10k : part_legnth = total_length //4
total_length < 1k : part_length = total_lenght //2
#function provide reasonable length string
#opened_file.read(X) -> X chars if available, or None if EOF
"take \n"
"take

" ['take', '\n']
import os
redact = opened_file.read('redeact.txt')  # "abc\n   " " "
redact_list = redact.split(" ")#['abc', '', '\n', '\t'
banned_words = set(opened_file.read("banned_words.txt"))
total_length = len(redact)
## partition based on length
part_length = total_length//2 #ttottal -> 100 
# search for the banned words
for i in range(0, part_length):
  if redact[i] in banned_words:
    redact[i] = "_REDEACTED_"
print(redact[:part_length+1])
    
  
# '   ' - > '','','',''


calculate avg of list then provide test cases
l = [1, 2, 3,4]
length = 0
for n in l:
  sum_of_list += n
  length += 1
  
avg = sum_of_lenght/( length) if length else 1
Time comeplxity - O(n)
test case 1 = []
test case 2= if it containes negative value
test case 3 : [0 ,0,0, 0]
test case 4: list of larger length
test case 5: [7, 8, 9,10]

  
  
koziakali
"""

def test_avg():
    test_cases = [
        ([1, 2, 3, 4], 2.5),
        ([5], 5.0),
        ([], 1),
        ([0, 0, 0, 0], 0.0),
        ([-1, -2, -3, -4], -2.5),
        ([1, -1, 2, -2, 3, -3], 0.0),
        ([1000000, 2000000, 3000000], 2000000.0),
        ([1.5, 2.5, 3.5, 4.5], 3.0),
    ]
    
    for i, (l, expected) in enumerate(test_cases):
        sum_of_list = 0
        length = 0

        for n in l:
            sum_of_list += n
            length += 1

        avg = sum_of_list / length if length else 1
        assert avg == expected, f"Test case {i+1} failed: expected {expected}, got {avg}"
        print(f"Test case {i+1} passed")

test_avg()
