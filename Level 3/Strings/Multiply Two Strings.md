# Multiply Two Strings

Asked in: **Microsoft, Google**

Given two numbers represented as strings, return multiplication of the numbers as a string.

    Note: The numbers can be arbitrarily large and are non-negative.
    Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.

For example,
given strings "12", "10", your answer should be “120”.

## Solution Approach

Would it be easier if you reversed the number for multiplication to calculate the reverse of the answer and then reverse it back to get the actual answer?

It is mostly simulation of the multiplication process where we take one number digit by digit and keep multiplying the digit with the other number and maintaining the sum in another array.

Make an array of res = ['0'..] of size n + m + 1

```
make j <-- m - 1 to 0
    carry = 0
    k = start
    i <-- n-1 to 0
        prod = A[i] * B[j]
        prev = res[k]
        s = (prev + prod + carry) % 10
        carry = (prev + prod + carry) / 10
        res[k] = s
```

Now reverse till non - zero integer

## Code

```python
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        n = len(A)
        m = len(B)
        res = ['0']*(n + m + 1)
        start = 0
        for j in range(m-1, -1, -1):
            k = start
            start += 1
            carry = 0
            for i in range(n-1, -1, -1):
                prod = int(A[i])*int(B[j])
                prev = int(res[k])
                s = (prev + prod + carry) % 10
                carry = int((prev + prod + carry) / 10)
                res[k] = str(s)
                k +=1
            res[k] = str(int(res[k]) + carry)
            k += 1
        while k > 0 and res[k] == '0':
            k -= 1
        for i in range(0, (k+1) // 2):
            res[i], res[k-i] = res[k-i], res[i]
        return ''.join(res)[:k+1]
```

## Much easier smaller faster code due to python optimisations

```python
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        A = int(A)
        B = int(B)
        return str(A*B)
```
