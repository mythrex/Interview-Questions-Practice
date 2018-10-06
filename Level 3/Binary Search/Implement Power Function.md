# Implement Power Function

Implement `pow(x, n) % d.`

In other words, given x, n and d,

find `(xn % d)`

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

```
Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
```

## Hint

You need to come up with a solution better than O(n).

Think recursively. You can think of an example like 3^8. How many multiplication do you really need to evaluate 3^8?

## Solution Approach

There are two major things to note here:

1. Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.

2. Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).

If n is even, note the following:

`x ^ n = (x \* x) ^ n/2`

Can you use the above observation to come up with a solution better than O(n)?

## Solution Approach 2

```python
def calcPow(self, x, n):
        if n == 0:
            return 1
        temp = self.calcPow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp
```

use the above function in **clever way**.
