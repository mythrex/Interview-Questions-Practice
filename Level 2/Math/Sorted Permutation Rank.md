# Sorted Permutation Rank

Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

**Example :**

```
The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
```

The answer might not fit in an integer, so return your answer % 1000003

## Hint

Enumerating all permutations and matching with the current one is going to be exponential.
Let's start by looking at the first character.
If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.
Number of permutation with a character C as the first character = number of permutation possible with remaining N-1 character = (N-1)!
Can you use the above information to get the rank of the current permutation ?

## Code

```python
class Solution:
    # @param A : string
    # @return an integer
    factorials = [0]*1000
    factorials[0] = factorials[1] = 1

    def factorial(self, n):
        if self.factorials[n]:
            return self.factorials[n]
        prod = 1
        for i in range(1,n+1):
            prod *= i
        self.factorials[n] = prod
        return prod

    def findRank(self, A):
        s = ''.join(sorted(A))
        i = 0
        j = 0
        res = 0
        while(i < len(A)):
            if A[i] == s[j]:
                s = s[0:j:1] + s[j+1:len(s):1]
                i += 1
                j = 0
            elif A[i] > s[j]:
                res += self.factorial(len(s) -1)
                j += 1
        return (res + 1) % 1000003
```

## Catch for faster Code

```
Consider example GEF
I = 0 G _ _ 2! Ways
No both E and F are < G
2! * 2 ways
I = 1 GE _ F > E
1! * 0 ways
Rank = 0 + 4
Return 4+1
```

## Faster Code

```python
class Solution:
    # @param A : string
    # @return an integer
    def fact (self, n ) :
        if n <= 1 :
            return 1
        else :
            return n * self.fact(n-1)

    def findRank(self, A):
        res = 1
        for i in range(0, len(A)) :
            rank = 0
            for j in range(i+1, len(A)) :
                if A[i] > A[j] :
                    rank += 1
            res = (res + rank * self.fact(len(A) - i - 1 ))%1000003
        return res
```
