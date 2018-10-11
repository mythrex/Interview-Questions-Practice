# Different Bits Sum Pairwise

Asked in: **Google**

_It is same as Sum of Pairwise Hamming Distance in LEVEL 2 MATH_

We define `f(X, Y)` as number of different corresponding bits in binary representation of X and Y. For example, f`(2, 7) = 2`, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so `f(2, 7) = 2.`

You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of `f(Ai, Aj)` for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 1000000007.

For example,

```
A=[1, 3, 5]

We return

f(1, 1) + f(1, 3) + f(1, 5) +
f(3, 1) + f(3, 3) + f(3, 5) +
f(5, 1) + f(5, 3) + f(5, 5) =

0 + 1 + 1 +
1 + 0 + 2 +
1 + 2 + 0 = 8
```

## Solution Approach

Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.
Lets say A = count of elements which are 0
and B = count of elements which are 1

In this case our answer is just 2AB, since each such pair contributes 1 to answer.

Can you combine this logic if we have multiple bits?

Note that all bits are independent in counting, since we are counting number of bits which are different in each pair.
So, we just do the same process for all different bits. Since Ai is an integer, we just have to do this for 31 different bits, so our solution is O(31\*N).

**To have clearly understand clearly you may check** _Sum of Pairwise Hamming Distance_

## Code

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        res = 0
        for i in range(32):
            mask = 1<<i
            x = 0
            y = 0
            for j in range(len(A)):
                if A[j] & mask:
                    y += 1
                else:
                    x += 1
            res += 2*x*y
        return res % 1000000007
```
