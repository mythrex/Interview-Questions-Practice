# Justified Text

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

## Example

```
words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

## Solution Approach

Corner Cases:

1. A line other than the last line might contain only one word. What should you do in this case?

In this case, that line should be left-justified.

2. Have you noticed that the last line is an exception in terms of spaces?

This is more of a simulation problem. The more elegant your code, the less chances of it being bug prone,

and more marks in the interview.

## Where I got stuck

Well consider the following input.

```
8 This is an example of text justiftion sd.
16
```

What will **the output** be?
I thought this would be output.

```
This    is    an
example  of text
justiftion   sd.
```

**But this was the output**

```
This    is    an
example  of text
justiftion sd.
```

_Observe the last line. There is only 1 space in between the words and rest of line has space_

### How to acheive this?

- Loop till you end of array
  - find the word count
  - check if length is less than **B**
  - To add space _this was the part that was confusing me_
    - check if this is last line _i + word_count < Array.size()_
    - else add no of space required in between words
  - add count if row has any space for _space_ character

## Code

```python
class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        n = len(A)
        # wc: word_count
        wc = 0
        # ls: length of string
        ls = 0
        res = []
        i = 0
        while i < n:
            ls = wc = 0
            # loop till len of string < B
            while i + wc < n and wc + ls + len(A[i + wc]) <= B:
                # add length of the word
                ls += len(A[i + wc])
                # increment word count
                wc += 1
            # till here yoy have find no of words that can be in a row
            # loop from i to i + wc
            temp = A[i]
            for j in range(0, wc - 1):
                # check if this is last line
                if i + wc >= n:
                    temp += ' '
                else:
                    # add no of spaces required
                    # sp: no of places in between words for spaces
                    # cl: character left
                    sp = wc - 1
                    cl = B - ls
                    # ( ((B - ls) // sp) + int(j < ((B - ls)%sp)) ) => no of spaces
                    temp += ' ' * ( (cl // sp) + int(j < (cl%sp)) )
                    # now add the word
                temp += A[i+j+1]
            # add no of space
            # this is we 0 if not last line
            temp += ' '*(B - len(temp))
            res.append(temp)
            i += wc
        return res
```
