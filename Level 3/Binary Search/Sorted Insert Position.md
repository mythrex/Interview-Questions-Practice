# Sorted Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

```
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
```

## Hint

You need to return the index of least element >= x.

## Solution Approach

After while loop in binary search is over. Think about the value of mid.

_What can you do with that_

```python
if A[mid] < B:
            return mid + 1
        else:
            return mid
```

## Code

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        low, high = 0, n - 1
        while low <= high:
            mid = (low+high)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        if A[mid] < B:
            return mid + 1
        else:
            return mid
```
