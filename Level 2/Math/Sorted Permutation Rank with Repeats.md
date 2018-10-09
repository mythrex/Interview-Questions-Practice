# Sorted Permutation Rank with Repeats

Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations.
Look at the example for more details.

**Example :**

```
Input : 'aba'
Output : 2

The order permutations with letters 'a', 'a', and 'b' :
aab
aba
baa
```

The answer might not fit in an integer, so return your `answer % 1000003`.

## Solution Approach

If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.
Number of permutation with a character C as the first character = number of permutation possible with remaining N-1 character = (N-1)! / (p1! _ p2! _ p3! ... ) where p1, p2, p3 are the number of occurrences of repeated characters.
For example, number of permutations possible with 3 ‘a’ and 3 ‘b’ is 6! / 3! 3! = 20
Hence,

```
rank = number of permutation possible with placing characters smaller than current first character in the first position + rank of permutation of string with the first character removed
```

So, we take a loop on the possibilities for the first character, and if that character is less than the current first character, we calculate the number of permutations using the formula given above (N-1)! / (p1! _ p2! _ p3! ... )
Now, there is a slight problem.
(N-1)! / (p1! _ p2! _ p3! ... ) does not necessarily fit in an integer. It is easy to calculate (N-1)! % MOD.
However, how do we handle divisions ? Modular_multiplicative_inverse is what you are looking for.
In short,

(1/A) % MOD = A ^ (MOD - 2) % MOD

## Solution

```py
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
        char_occur = {}
        for char in A:
            char_occur[char] = char_occur.get(char, 0) + 1
        for i in range(0, len(A)-1) :
            rank = 0
            for j in range(i+1, len(A)) :
                if A[i] > A[j] :
                    rank += 1
            temp = self.fact(len(A) - i - 1)%1000003
            temp1= 1
            for key in char_occur.keys() :
                temp1 *= self.fact(char_occur[key])
            temp1 = pow(temp1, 1000001, 1000003)
            res = (res + rank * temp1 * temp)%1000003
            char_occur[A[i]] -= 1
        return res
```

## Complexity

`O(n^2)`
