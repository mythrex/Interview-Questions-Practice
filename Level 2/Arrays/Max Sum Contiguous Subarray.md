# Max Sum Contiguous Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

**For example:**
`Given the array [-2,1,-3,4,-1,2,1,-5,4],`
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
For this problem, return the maximum sum.

# My Code

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        dp_mat = [[0 for x in range(n)] for y in range(n)]
        max_no = -float('inf')
        for i in range(n):
            if max_no < A[i]:
                    max_no = A[i]
            dp_mat[0][i] = A[i]
        for i in range(1, n):
            for j in range(n - i):
                dp_mat[i][j] = dp_mat[i - 1][j] + A[i+j]
                if max_no < dp_mat[i][j]:
                    max_no = dp_mat[i][j]
        return max_no
```

## Complexity

`O(n^2)`

## Solution Approach

Let us say Ai, Ai+1 … Aj is our optimal solution.
Note that no prefix of the solution will ever have a negative sum.
Let us say Ai … Ak prefix had a negative sum.

```
Sum ( Ai Ai+1 … Aj ) = Sum (Ai … Ak) + Sum(Ak+1 … Aj)
Sum ( Ai Ai+1 … Aj) - Sum(Ak+1 … Aj) = Sum(Ai … Ak)
Now, since Sum(Ai … Ak) < 0,
Sum (Ai Ai+1 … Aj) - Sum (Ak+1 … Aj) < 0
which means Sum(Ak+1 … Aj ) > Sum (Ai Ai+1 … Aj)
```

This contradicts the fact that Ai, Ai+1 … Aj is our optimal solution.
Instead, Ak+1, Ak+2 … Aj will be our optimal solution.
Similarily, you can prove that for optimal solution, it is always good to include a prefix with positive sum.
Try to come up with a solution based on the previous 2 facts.

If this still does not make sense, watch this video for more detailed explanation :

## Improved Code

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        max_so_far = -float('inf')
        max_ending_here = 0
        for i in xrange(n):
            max_ending_here += A[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                    max_ending_here = 0
        return max_so_far
```
