# Kth Row of Pascal's Triangle

Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

**Example,**

```
Input : k = 3

Return : [1,3,3,1]
```

**NOTE:** k is 0 based. k = 0, corresponds to the row [1].

## Code

```py
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        res = [0 for i in range(A + 1)]
        temp = [0 for i in range(A + 1)]
        res[0],res[1] = 1, 1
        for i in range(2, A + 1):
            for j in range(i + 1):
                if j == 0:
                    temp[0] = 1
                else:
                    temp[j] = res[j] + res[j - 1]
            res = list(temp)
        return res
```

## Fastest Code Approach

```
For A = 3
res= [1,1]
Do this 2 times
    Res = [1] + [res[i] + res[i+1] for 0 to res.length - 1] +[1]
```

## Fastest Code

```py
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A < 0:
            return []
        if A == 0:
            return [1]

        res = [1,1]
        for _ in range(A - 1):
            res = [1] + [res[i]+res[i + 1] for i in range(len(res) - 1)] + [1]
        return res
```
