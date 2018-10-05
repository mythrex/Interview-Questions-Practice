# Matrix Search

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

```
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than or equal to the last integer of the previous row
```

**Example:**

Consider the following matrix:

```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```

Given `target = 3`, return 1 ( 1 corresponds to true )

Return `0 / 1` ( 0 if the element is not present, 1 if the element is present ) for this problem

## Hint

Look at the matrix properties carefully. Basically you are given the elements in sorted order already. How can you exploit this property now?

## Hint 2

If you write down the numbers of row 1 followed by numbers in row2, row3 and so on, do you think the resulting array would be sorted ?
If yes, how do you search for a number efficiently in a sorted array ?

## Solution Approach

The solution is simple

```
low, high = 0, row*column

check if A[i][j] == B
    return 1

i = mid // column
j = mid % column
```

## Code

```python
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        r = len(A)
        c = len(A[0])
        low, high = 0, r*c - 1
        while low <= high:
            mid = (low + high) // 2
            i = mid // c
            j = mid % c
            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                low = mid + 1
            else:
                high = mid - 1
        return 0
```
