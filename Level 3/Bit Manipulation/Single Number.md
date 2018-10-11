# Single Number

Asked in: **Amazon**

Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example :**

```
Input : [1 2 2 3 1]
Output : 3
```

## Solution Approach

We have noticed that if X has 1 in that position, we will have odd number of 1s in that position.

If X has 0 in that position, we will have odd number of 0 in that position.

If you look at the bit operators, XOR is exactly what we need.

XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0.

Finally, there is only one number left.

`A ^ A = 0 and A ^ B ^ A = B.`

So, all even occurences will cancel out using XOR.

## Code

```py
from functools import reduce
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x,y: x^y, A)
        # BADE ARAAM SE
```
