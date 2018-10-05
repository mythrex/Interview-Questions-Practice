# Excel Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

**For example:**

```
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
```

## The Catch

You need to subtract 26 when rem == 0, this is because suppose A = 26
Then

```
Rem = 0
Res = ‘Z’
A = 1
Rem = 1
Res = ‘ZA’
A = 0
```

## My Solution

```python
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        res = ''
        T = dict(zip([i for i in range(26)], 'ZABCDEFGHIJKLMNOPQRSTUVWXY'))
        while(A > 0):
            rem = A % 26
            res = T[rem] + res
            A = int(A / 26)
        return res
```
