# Min XOR value

Asked in: **Booking.com**

Given an array of N integers, find the pair of integers in the array which have minimum `XOR` value. Report the minimum `XOR` value.

**Examples :**

```
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
```

## Hint

Sort the array.

## Hint 2

The brute-force would be to try every pair `(x, y)`. If the array is sorted, do you need to check for every pair? Try to reduce the number of checked pairs.

## Solution Approach

The first step is to sort the array. The answer will be the minimal value of X[i] XOR X[i+1] for every i.

Proof:
Let’s suppose that the answer is not X[i] XOR X[i+1], but A XOR B and there exists C in the array such as A <= C <= B.

Next is the proof that either A XOR C or C XOR B are smaller than A XOR B.

```
Let A[i] = 0/1 be the i-th bit in the binary representation of A
Let B[i] = 0/1 be the i-th bit in the binary representation of B
Let C[i] = 0/1 be the i-th bit in the binary representation of C
```

This is with the assumption that all of A, B and C are padded with 0 on the left until they all have the same length

Example: A=169, B=187, C=185

```
A=10101001
B=10111011
C=10111001
```

Let i be the leftmost (biggest) index such that A[i] differs from B[i]. There are 2 cases now:

```
1) C[i] = A[i] = 0,
then (A XOR C)[i] = 0 and (A XOR B)[i] = 1
This implies (A XOR C) < (A XOR B)
2) C[i] = B[i] = 1,
then (B XOR C)[i] = 0 and (A XOR B)[i] = 1
This implies (B XOR C) < (A XOR B)
```

Time complexity: `O(N * logN)` to sort the array and `O(N)` to find the smallest XOR
Space complexity: `O(N)`

## Code

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        val = float('inf')
        A = sorted(A)
        for i in range(len(A)-1):
            val=min(val, A[i] ^ A[i+1])

        return val
```
