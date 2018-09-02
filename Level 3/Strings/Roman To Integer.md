# Roman To Integer

Asked in: **Amazon, Facebook, Microsoft, Twitter**

## Question

```
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14

Input : "XX"
Output : 20
```

## Solution Approach

Take an example of XVI and XIV

```
XVI = 10 + 5 + 1
XIV = 10 -1 + 5
Whenever **val(A[i]) >= val(A[i+1])**
    **res = res + val(A[i])**
    i += 1

else:
    ** res = res - val[A[i]] + val[i+1]**
    i += 2
```

## Code

```python
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        val = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        num = 0
        n = len(A)
        i = 0
        while(i<n):
            s1 = val[A[i]]
            if i + 1 < n:
                s2 = val[A[i+1]]
                if s1 >= s2:
                    num += s1
                    i += 1
                else:
                    num += (s2-s1)
                    i += 2
            else:
                num += s1
                i += 1
            # print(i, A[i], val[A[i]],num)
        return num
```
