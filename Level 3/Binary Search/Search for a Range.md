# Search for a Range

Asked in: **Google, Amazon**

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of `O(log n)`.

If the target is not found in the array, return `[-1, -1]`.

**Example**:

Given `[5, 7, 7, 8, 8, 10]`

and target value `8`,

return `[3, 4]`.

## Hint

The problem can be simply broken down as two binary searches for the begining and end of the range, respectively.

## Approach

Pass and argument `search_first`

```python
if A[mid] == B:
    res = mid
    if search_first:
        high = mid - 1
    else:
        low = mid + 1
```

and rest of binary search is same.

## Code

```python
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def binSearch(self, A, B, search_first):
        res = -1
        n = len(A)
        low, high = 0 , n - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] == B:
                res = mid
                if search_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        return res
    def searchRange(self, A, B):
        first = self.binSearch(A, B, True)
        last = self.binSearch(A, B, False)
        return [first, last]
```
