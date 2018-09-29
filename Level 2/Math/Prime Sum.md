# Prime Sum

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read [Goldbach’s conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)

Example

```
Input : 4
Output: 2 + 2 = 4
```

## The Trick

Make array of is_primes till A

```
If is_primes[i] and is_primes[A - i]
    Return [is_primes[i], is_primes[A-i]]
```

## Code

```python
class Solution:
    def primesum(self, n: int) -> 'List[int]':
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False

        for i in range(2, n):
            if is_prime[i] and is_prime[n - i]:
                return [i, n - i]

        return []
```

## Complexity

`O(n)`
