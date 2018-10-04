# Distinct Characters Substring

Given a string, find the smallest window length with all distinct characters of the given string. For eg. str = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca”

**For example,**
`in “aabcbcdb”, the smallest string that contains all the characters is “abcbcd”.`

This problem reduces to [Find the smallest window in a string containing all characters of another string](https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/).

In that problem we find the smallest window that contains all the characters of given pattern.

1. Count all distinct characters in given string.
2. Now follow the algorithm discussed in below post.

## Code

```python
def distinctCharSubString(S):
    n = len(S)
    # len of distinct Characters
    dist = len(set(S))
    curr_count = dict(zip('abcdefghijklmnopqrstuvwxyz', [0]*26))
    min_len = float('inf')
    start = 0
    cur_dist_count = 0
    for i in range(n):
        curr_count[S[i]] += 1
        # if distinct char
        if curr_count[S[i]] == 1:
            cur_dist_count += 1
        # if found all the distinct chars
        if cur_dist_count == dist:
            # if first letter of window count > 1
            # minimize window
            while curr_count[S[start]] > 1:
                curr_count[S[start]] -= 1
                start += 1
            win_len = i - start + 1
            min_len = min(min_len, win_len)
    return S[start:start+min_len]
```
