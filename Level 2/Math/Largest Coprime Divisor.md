# Largest Coprime Divisor

You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

- X divides A i.e. A % X = 0
- X and B are co-prime i.e. gcd(X, B) = 1

**For example,**

```
A = 30
B = 12
We return
X = 5
```

## Hint

We know A is the greatest number dividing A. So if A and B are coprime, we can return the value of X to be A. Else, we can try to remove the common factors of A and B from A.
Given this hint, how would you think of the solution ?

## My Solution

```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B < A :
            # swap
            temp = A
            A = B
            B = temp
        while A > 0:
            temp = A
            A = B % A
            B = temp
        return temp

    def cpFact(self, A, B):
        gcd = self.gcd(A, B)
        if gcd == 1:
            return A
        A /= gcd
        return self.cpFact(A, B)
```

## Way to Fastest Solution

You can find gcd in following way

```py
while True:
A1 = A;
B1 = B;
while B1>0:
A1,B1 = B1,A1%B1;
Return A1
#A1 will be gcd(A, B)
```

## Fastest Solution

```py
def cpFact(self, A, B):
        while True:
            A1 = A;
            B1 = B;
            while B1>0:
                A1,B1 = B1,A1%B1;
            if A1==1:
                return A;
            A = A//A1;
#same as A /= gcd
```
