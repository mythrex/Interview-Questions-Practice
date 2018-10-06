# Rotated Array

Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

`(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).`

Find the minimum element.

The array will not contain duplicates.

```
"NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?"
```

## PROBLEM APPROACH:

If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].

Lets look at how we can calculate the number of times the array is rotated.

[Watch this video for complete solution](https://youtu.be/4qjprDkJrjY)

## Code

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        low, high = 0, n - 1
        res = -1
        while(low <= high):
            mid = (low + high) // 2
            if A[low] <= A[high]:
                res = A[low]
                break
            elif A[mid] <= A[low] and A[mid] <= A[high]:
                res = A[mid]
                break
            elif A[mid] >= A[low]:
                low = mid + 1
            elif A[mid] <= A[high]:
                high = mid - 1
        return res
```
