# Square Root of Integer

Asked in: **Amazon, Google, Facebook**

Implement `int sqrt(int x)`.

Compute and return the square root of x.

If x is not a perfect square, return `floor(sqrt(x))`

**Example**

```
Input : 11
Output : 3
```

## Solution Approach 1

A Simple Solution to find floor of square root is to try all numbers starting from 1. For every tried number i, if i*i is smaller than x, then increment i. We stop when i*i becomes more than or equal to x. Below is the implementation of above idea.

## Code 1

```python
# Python3 program to find floor(sqrt(x)

# Returns floor of square root of x
def floorSqrt(x):

    # Base cases
    if (x == 0 or x == 1):
        return x

    # Staring from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1; result = 1
    while (result <= x):

        i += 1
        result = i * i

    return i - 1

# Driver Code
x = 11
print(floorSqrt(x))
```

## Solution Approach 2

Think in terms of binary search.

Let us say S is the answer.

We know that 0 <= S <= x.

Consider any random number r.

```
    If r*r <= x, S >= r

    If r*r > x, S < r.
```

Maybe try to run a binary earch for S.

## Code 2 using Binary Search

```python
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        start, end = 1, A
        while(start <= end):
            mid = (start + end) // 2
            if mid*mid == A:
                return mid
            elif mid*mid < A:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans
```
