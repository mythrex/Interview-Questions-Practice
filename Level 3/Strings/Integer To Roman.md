# Integer to Roman

Asked in: **Amazon, Facebook, Microsoft, Twitter**

Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

```
Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
```

## Solution Approach

```
It is very much like learning our own number system.

All you need to know is how to write 0-9, 10, 20, 30, 40, .. 90, 100, 200, 300,… 900, 1000, 2000, 3000.

You can derive rest of the numbers using the above.
```

## Code

```python
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        rom_num = ''
        while A > 0:
            for _ in range(A // val[i]):
                rom_num += sym[i]
                A = A - val[i]
            i += 1
        return rom_num
```
