# Count Element Occurence

Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example :**

```
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.
```

## PROBLEM APPROACH :

[Watch this video](https://youtu.be/pLT_9jwaPLs)

## Code

```python
def countNoOfReferences(arr, num, search_first=True):
    n = len(arr)
    res = -1
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            res = mid
            if search_first:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return res

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, arr, num):
        first = countNoOfReferences(arr, num, True)
        if first != -1:
            last = countNoOfReferences(arr, num, False)
            return (last - first + 1)
        else:
            return (0)
```
