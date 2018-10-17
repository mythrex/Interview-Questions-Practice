# Repeat and Missing Number Array

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

**Note:** Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Note:** that in your output A should precede B.

**Example:**

```
Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4
```

## My Approach

D = sum(A) - sum(n)
F = prod(A) - n!
B = D / (F - 1)
A = D + B

## The problem

Division and multiplication are heavy task. It may fail for large nos.

## The improvement

```
Sum(Actual) = Sum(1...N) + A - B

Sum(Actual) - Sum(1...N) = A - B.

Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B)

= (Sum(Actual) - Sum(1...N)) ( A + B).
```

## The Code

```py
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        fac_n = 1
        prod = 1
        # sum of elem of A
        s = 0
        s2 = 0
        sum_n = n * (n + 1) / 2
        sum_n2 = sum_n * (2*n + 1) / 2
        for i in range(len(A)):
            # prod *= A[i]
            # fac_n *= (i + 1)
            s += A[i]
            s2 += A[i]**2
        D = s - sum_n
        # print(D)
        # F = prod / fac_n
        F = s2 - sum_n2
        E = F / D
        # print(F)
        # B = round(D / (F - 1))
        # A = round(D + B)
        A = (D + E) / 2
        B = (E - D) / 2
        return [A, B]
```
