# Matrix Median

Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N\*M is odd.

For example,

```
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
```

**Note:** No extra memory is allowed.

## Hint

We cannot use extra memory, so we can’t actually store all elements in an array and sort the array.
But since, rows are sorted it must be of some use, right?

Note that in a row you can binary search to find how many elements are smaller than a value X in O(log M).

```python
 place = 0
for i in range(r):
    place += bisect_right(A[i], mid)
```

## Solution Approach

Well Consider the following matrix and sort A.

```
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
```

We will be maintaining

`low = lowest in matrix`

`high = highest in matrix`

`mid = (low + high)//2`

median will always at (r\*c+1)//2

Find the place where this mid should be placed.

```python
if place < req:
    low = mid + 1
else:
    high = mid
```

continue this till `low < mid`

## Code

```python
from bisect import bisect_right

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        r = len(A)
        c = len(A[0])
        low = float('inf')
        high = -float('inf')
        for i in range(r):
            low = min(A[i][0], low)
            high = max(A[i][c-1], high)
        req = (r*c + 1) // 2
        while low < high:
            mid = (low + high) // 2
            place = 0
            for i in range(r):
                place += bisect_right(A[i], mid)
            if place < req:
                low = mid + 1
            else:
                high = mid
        return low
```
