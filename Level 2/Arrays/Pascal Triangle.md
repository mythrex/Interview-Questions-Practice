# Pascal Triangle

Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

**Example,**
Given numRows = 5,
Return

```
[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
```

## Solution Approach

num at position i = number at position i in prev row + number at position (i + 1) in previous row.
Now, note that to calculate num at position i, we need the numbers in previous row. Which means it makes sense to create rows in order.
Create a 2D matrix where Matrix[r] denotes row r.
Now process the rows starting from row number 1.
Row number 1 is obviously just 1.

`For Row i, Row[i][0] = Row[i][i] = 1. And Row[i][j] = Row[i-1][j] + Row[i-1][j-1], when j belongs to [1, i)`

## Code

```py
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        p_tri = [[0 for i in range(A)] for j in range(A)]
        # make the matrix
        for i in range(A):
            p_tri[i][0]  = p_tri[i][i] = 1
            for j in range(i + 1):
                if i != j and j > 0 :
                    p_tri[i][j] = p_tri[i - 1][j -1] + p_tri[i -1][j]
        # return the result
        res = []
        for i in range(A):
            a = []
            for j in range(i + 1):
                a.append(p_tri[i][j])
            res.append(a)
        return res
```
