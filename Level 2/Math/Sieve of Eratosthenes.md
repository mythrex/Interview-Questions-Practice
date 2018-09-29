# Sieve of Eratosthenes

Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

Example

```
Input : n =10
Output : 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19
```

## The Trick

Make all the multiples of primes in array equal to false

## Code

```python
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes = [True for i in xrange(0, A + 1)]
        primes[0] = primes[1] = False
        for i in xrange(2, int((A)**0.5)+1):
            if primes[i] == True:
                j = 2
                while(i * j <= A):
                    primes[i * j] = False
                    j += 1
        primes_till_A = []
        for i in xrange(0, len(primes)):
            if primes[i]:
                primes_till_A.append(i)
        return primes_till_A
```

## Complexity

`O(nlog(logn))`

## Link to video

[Link to video to Seive of Eratosthenes](https://youtu.be/eKp56OLhoQs?list=PL2_aWCzGMAwLL-mEB4ef20f3iqWMGWa25)
