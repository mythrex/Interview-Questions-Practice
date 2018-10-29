# Flip

You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

**Notes:**

`Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.`

**For example,**

```
S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
```

**Another example,**

```
If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
```

## Approach

Well, looking at problem it does not look how to tackle.
We need to calc the difference in increase in 1s if we flip all the bits till that index.
0 = 1
1 = - 1( because flipping 1 will cause a 0)
Now array becomes 1,-1 array
Now simply return the max sum array.

It was difficult for me to figure out how to calc L, R for that use s =i + 1 if cur < 0.

## Code

```py
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        L = 0
        R = 0
        s = 0
        cur_change = 0
        max_change = 0
        # kaden's algorithm
        for i in range(len(A)):
            val = -1 if A[i] == "1" else 1
            cur_change += val
            # print(cur_change)
            if max_change < cur_change:
                max_change = cur_change
                L = s + 1
                R = i + 1
            # print('maxchange:', max_change, L, R)
            if cur_change < 0:
                cur_change = 0
                s = i + 1
        res = []
        if L!=0 and R != 0:
            return [L, R]
        return res
```
