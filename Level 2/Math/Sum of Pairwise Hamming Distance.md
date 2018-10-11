# Sum of pairwise Hamming Distance

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

**For example,**

```
HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).
Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.
Example
Let f(x, y) be the hamming distance defined above.
```

A=[2, 4, 6]

```
We return,
f(2, 2) + f(2, 4) + f(2, 6) +
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) =
```

```
0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
```

## The Catch

The naive method fails because I was iterating the loop and the complexity was O(n2)

## The Naive Method

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def f(self, a, b):
        z = a ^ b
        r = 0
        while z > 0:
            r += z & 1
            z >>= 1
        return r

    def hammingDistance(self, A):
        res = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i] != A[j]:
                    res += self.f(A[i], A[j])
        return res % 1000000007
```

## The Improvement

Suppose the given array contains only binary numbers, i.e A[i] belongs to [0, 1].
Let X be the number of elements equal to 0, and Y be the number of elements equals to 1.
Then, sum of hamming distance of all pair of elements equals 2XY, as every pair containing one element from X and one element from Y contribute 1 to the sum.
As A[i] belongs to [0, 2^31 - 1] and we are counting number of different bits in each pair, we can consider all the 31 bit positions independent.
For example:

```
A = [2, 4, 6] = [010, 100, 110]
At bit position 0 (LSB): x = 3, y = 0
At bit position 1: x = 1, y = 2
At bit position 2(MSB): x = 1, y = 2
Total sum = number of pairs having different bit at each bit-position = (2 _ 3 _ 0) + (2 _ 1 _ 2) + (2 _ 1 _ 2) = 8
```

**Time complexity: O(N)
Space complexity: O(1)**

## The Code

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        res = 0
        for i in range(30):
            mask = 1 << i
            x = 0
            y = 0
            for index in xrange(len(A)):
                if A[index] & mask:
                    y += 1
                else:
                    x += 1
            res += 2*x*y
        return res % 1000000007
```
