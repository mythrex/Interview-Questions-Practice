# Find Duplicate in Array

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
Sample Input:
`[3 4 1 4 1]`

Sample Output:
`1`

If there are multiple possible answers ( like in the sample case above ), output any one.
If there is no duplicate, output -1

## Solution Approach

Make array = [True True True True True]
Make array[i] = false if we encounter array[i]
If array[i] = false means we already visited it

```py
class Solution: # @param A : tuple of integers # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        V = [ True for i in range(n)]
        for i in range(n):
            if V[A[i]]:
                V[A[i]] = False
            else:
                return A[i]
                return -1
```

Solution Approach 2
Sum of all elems = S
Sum of all int 1 .. n = n\*n+½
Missing = S - sum of 1..n

```py
class Solution: # @param A : tuple of integers # @return an integer
    def repeatedNumber(self, A):
        s = sum(A)
        n = len(A)
        missing = s - (n\*(n-1))/2
        return missing
```

Some other methods can be found at [geeksforgeeks](https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/)

## The Xor Method

### Method 3 (Make two equations)

Let the numbers which are being repeated are X and Y. We make two equations for X and Y and the simple task left is to solve the two equations.
We know the sum of integers from 1 to n is n(n+1)/2 and product is n!. We calculate the sum of input array, when this sum is subtracted from n(n+1)/2, we get X + Y because X and Y are the two numbers missing from set [1..n]. Similarly calculate product of input array, when this product is divided from n!, we get X*Y. Given sum and product of X and Y, we can find easily out X and Y.
Let summation of all numbers in array be S and product be P
X + Y = S – n(n+1)/2
XY = P/n!
Using above two equations, we can find out X and Y. For array = 4 2 4 5 2 3 1, we get S = 21 and P as 960.
X + Y = 21 – 15 = 6
XY = 960/5! = 8
X – Y = sqrt((X+Y)^2 – 4*XY) = sqrt(4) = 2
Using below two equations, we easily get X = (6 + 2)/2 and Y = (6-2)/2
X + Y = 6
X – Y = 2
Thanks to geek4u for suggesting this method. As pointed by Beginner , there can be addition and multiplication overflow problem with this approach.
The methods 3 and 4 use all useful information given in the question 🙂
