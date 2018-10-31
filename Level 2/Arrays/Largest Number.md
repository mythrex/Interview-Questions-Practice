# Largest Number

Asked in **Amazon and Goldman Sachs**

Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given `[3, 30, 34, 5, 9]`, the largest formed number is 9534330.
**Note:** The result may be very large, so you need to return a string instead of an integer.

## Solution Approach

Sorting all numbers in descending order is the simplest solution that occurs to us. But this doesn’t work.
For example, 548 is greater than 60, but in the output, 60 comes before 548. As a second example, 98 is greater than 9, but 9 comes before 98 in the output.

The solution is to use any comparison based sorting algorithm. Thus, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers.

Given two numbers X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y).

If XY is larger, then, in the output, X should come before Y, else Y should come before X.
For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.

## Code

```py
from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = map(A, str)
        key = cmp_to_key(lambda x,y: 1 if x + y >= y + x else -1)
        res = ''.join(sorted(A, key= key, reverse=True))
    # removes left zeroes
        res = res.lstrip('0')
        return res if res else 0
```

## Another approach that does not require cmp_to_key

Now suppose A = [2402,3489, 10, 4, 6, 66, 3]
Now we compute key = [24022402, 348934893, 10101010, 44444444, 66666666, 6666666, 33333333]

Key = i*(maxLen * 2 // len(i) )

We are checking making the if alphabetically key is bigger or not

‘24022402’ < ‘348934893’

‘30003000’ > ‘2000020000’

## Code

```py
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        maxlen = len(str(max(A)))
        if all(v == 0 for v in A):
            return '0'
        for i in A:
            print(i, str(i) * (maxlen * 2 // len(str(i)) ))
        return ''.join(sorted((str(v) for v in A), reverse=True, key=lambda i: i*(maxlen * 2 // len(i))))
```
