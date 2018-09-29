# Count No of occurances

Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)

## Solution Approach 1

Linearly search for x, count the occurrences of x and return the count.

## Solution Approach 2

We first find an occurrence using binary search. Then we match toward left and right sides of the matched the found index.

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


arr = [1, 1, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 5]
num = 2
first = countNoOfReferences(arr, num, True)
if first != -1:
    last = countNoOfReferences(arr, num, False)
    print(last - first + 1)
else:
    print(-1)
```
