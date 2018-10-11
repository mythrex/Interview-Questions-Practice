# Divide Integers

Asked in: **Microsoft, Amazon**

Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:
`5 / 2 = 2`

Also, consider if there can be overflow cases. For overflow case, return INT_MAX.

## Hint

dividend = answer \* divisor + c

You need to find the answer here without using any of the operators mentioned in the question. Think about the binary expansion of answer.

We can work with bits without using the standard operators. If you can find what bits are set in answer you will be done.

## Solution Approach

Think in terms of bits.

How do you do the division with bits?

    `How do you determine the most significant bit in the answer?`

Iterate on the bit position ‘i’ from 31 to 1 and find the first bit for which divisor«i is less than dividend.

    `How do you use (1) to move forward in similar fashion?`

## Code

```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        temp = 0
        quotient = 0
        sign = -1 if ((A < 0) ^ (B < 0)) else 1
        A, B = abs(A), abs(B)
        for i in range(31, -1, -1):
            if (temp + (B << i)) <= A:
                temp += B << i
                quotient |= 1 << i
        return sign * quotient
```
