# Rotated Sorted Array Search

Asked in: **Facebook, Google, Microsoft**

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

`(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 )`.

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

```
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

        NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
```

## Hint

Think a modified version of the binary search.
If the pivot is known, the binary search becomes trivial as the array to the either side of the pivot is sorted.
Can you somehow search for the pivot in your binary search?

## Solution Approach

Input arr[] = {3, 4, 5, 1, 2}

Element to Search = 1

1. Find out pivot point and divide the array in two
   sub-arrays. (pivot = 2) _Index of 5_
2. Now call binary search for one of the two sub-arrays.
   - If element is greater than 0th element then
     search in left array
   - Else Search in right array
     (1 will go in else as 1 < 0th element(3))
3. If element is found in selected sub-array then return index
   Else return -1.

## Code

```python
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binSearch(self, A, B):
        l, r = 0, len(A)-1
        while l <= r:
            mid = (l + r)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                l = mid+1
            elif A[mid] > B:
                r = mid-1
        return -1

    def findPivot(self, A):
        low, high = 0, len(A)-1
        res = -1
        while low <= high:
            mid = (low+high)//2
            if A[low] <= A[high]:
                res = low
                break
            elif A[low] <= A[mid] and A[mid] <= A[high]:
                res = mid
                break
            elif A[mid] >= A[low]:
                low = mid+1
            elif A[mid] <= A[high]:
                high = mid-1
        return res

    def search(self, A, B):
        n = len(A)
        pivot = self.findPivot(A)
        # print(pivot)
        res1 = self.binSearch(A[0:pivot], B)
        res2 = self.binSearch(A[pivot:n], B)
        if res2 != -1:
            res2 += pivot
        return max(res1, res2)
```

## Solution Approach 2

We can search an element in one pass of Binary Search. The idea is to search

1. Find middle point mid = (l + h)/2
2. If key is present at middle point, return mid.
3. Else If arr[l..mid] is sorted
   - If key to be searched lies in range from arr[l]
     to arr[mid], recur for arr[l..mid].
   - Else recur for arr[mid+1..r]
4. Else (arr[mid+1..r] must be sorted)
   - If key to be searched lies in range from arr[mid+1]
     to arr[r], recur for arr[mid+1..r].
   - Else recur for arr[l..mid]

## Code 2

```python
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binSearch(self, A, l, r, B):
        if l > r:
            return -1
        mid = (l+r)//2
        if A[mid] == B:
            return mid
        # if A{l...mid] is sorted
        if A[l] <= A[mid]:
            # if B lies in A[l..mid-1]
            if B <= A[mid] and B >= A[l]:
                return self.binSearch(A, l, mid-1, B)
            return self.binSearch(A, mid+1, r, B)
        # if B lies in A[]
        if B >= A[mid] and B <= A[r]:
            return self.binSearch(A, mid+1, r, B)
        return self.binSearch(A, l, mid-1, B)

    def search(self, A, B):
        return self.binSearch(A, 0, len(A)-1, B)
```
