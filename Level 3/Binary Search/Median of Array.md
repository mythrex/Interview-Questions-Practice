# Median of Array

Asked in: **Amazon, VMWare, Google, Microsoft**

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be `O(log (m+n))`.

```
Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
```

```
    NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element.
    For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
```

## Hint

The expected time complexity gives away binary search in this case.
We are going to do binary search for the answer in this case.

Given a sorted array A of length m, we can split it into two parts:
`{ A[0], A[1], … , A[i - 1] } { A[i], A[i + 1], … , A[m - 1] }`

All elements in right part are greater than elements in the left part.

The left part has i elements, and right part has m - i elements.
There are m + 1 kinds of splits.

(i = 0 ~ m)

When i = 0, the left part has “0” elements, the right part has “m” elements.
When i = m, the left part has “m” elements, right part has “0” elements.

For the array B, we can split it in the same way:
`{ B[0], B[1], … , B[j - 1] } { B[j], B[j + 1], … , B[n - 1] }`

The left part has “j” elements, and right part has “n - j” elements.

Put A’s left part and B’s left part into one set. (Let’s name this set “LeftPart”)

Put A’s right part and B’s right part into one set. (Let’s name this set”RightPart”)

```
        LeftPart           |            RightPart

{ A[0], A[1], … , A[i - 1] } 	{ A[i], A[i + 1], … , A[m - 1] }
{ B[0], B[1], … , B[j - 1] } 	{ B[j], B[j + 1], … , B[n - 1] }
```

If we can ensure the following:

```
        LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
        All elements in RightPart is greater than elements in LeftPart,
```

then we can split all elements in {A, B} into two parts with equal length, and one part is always greater than the other part.

Then the median can thus be easily found.

    Based on condition 1, can you derive the value of j if value of i is known?
    Can you binary search on i ?

## Code

```python
from bisect import bisect_right
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedian(self, A, B, req):
        n = len(A)
        m = len(B)
        max1, max2 = 0, 0
        min1, min2 = 0, 0
        if n > 0:
            max1 = A[n-1]
            min1 = A[0]
        if m > 0:
            max2 = B[m-1]
            min2 = B[0]
        low, high = min(min1, min2), max(max1, max2)
        while low < high:
            mid = (low+high)//2
            place = 0
            place += bisect_right(A, mid)
            place += bisect_right(B, mid)
            if place < req:
                low = mid + 1
            else:
                high = mid
        return int(low)

    def findMedianSortedArrays(self, A, B):
        n = len(A)
        m = len(B)
        is_even = False
        if (n + m) % 2:
            req = (n+m)//2 + 1
        else:
            req = (n+m)/2
            is_even = True
        # print(req)
        res = 0
        if is_even:
            res = float(self.findMedian(A, B, req) + self.findMedian(A, B, req+1)) / 2
        else:
            res = self.findMedian(A,B,req)
        return res
```
