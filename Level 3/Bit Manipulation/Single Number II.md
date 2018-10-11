# Single Number II

Asked in: **Google, Amazon**

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

```
Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
```

## Solution Approach

Having noticed that if X has 1 in that position, we will have 3x+1 number of 1s in that position. If X has 0 in that position, we will have 3x+1 number of 0 in that position.

A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit.

We can improve this based on the previous solution using three bitmask variables:

ones as a bitmask to represent the ith bit had appeared once.
twos as a bitmask to represent the ith bit had appeared twice.
threes as a bitmask to represent the ith bit had appeared three times.
When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0. The final answer will be the value of ones.

## Code

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in range(32):
            s = 0
            for j in range(len(A)):
                if (A[j]>>i) & 1:
                    s += 1
                    s %= 3
            if s != 0:
                res |= s << i
        return res
```
