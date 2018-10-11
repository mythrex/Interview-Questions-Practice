# Reverse Bits

Reverse bits of an 32 bit unsigned integer

Example 1:

```
x = 0,

          00000000000000000000000000000000
=>        00000000000000000000000000000000
```

return 0

Example 2:

```
x = 3,

          00000000000000000000000000000011
=>        11000000000000000000000000000000
```

return 3221225472

## Hint

How do you swap the ‘i’th bit with the ‘j’th bit?

Try to figure out if you could use the XOR operation to do it.

## Solution Approach

Reversing bits could be done by swapping the n/2 least significant bits with its most significant bits.

The trick is to implement a function called swapBits(i, j), which swaps the ‘i’th bit with the ‘j’th bit.

If you still remember how XOR operation works:

```
0 ^ 0 == 0,
1 ^ 1 == 0,
0 ^ 1 == 1, and
1 ^ 0 == 1.
```

We only need to perform the swap when the ‘i’th bit and the ‘j’th bit are different.

To test if two bits are different, we could use the XOR operation. Then, we need to toggle both ‘i’th and ‘j’th bits.

We could apply the XOR operation again.

By XOR-ing the ‘i’th and ‘j’th bit with 1, both bits are toggled.

Bonus approach (The divide and conquer approach):

Remember how merge sort works? Let us use an example of n == 8 (one byte) to see how this works:

```
              01101001

             /        \

           0110       1001

          /   \       /   \

         01    10    10    01

        /\     /\    /\     /\

       0  1   1  0  1  0   0  1
```

The first step is to swap all odd and even bits. After that swap consecutive pairs of bits, and so on …

Therefore, only a total of log(n) operations are necessary.

**Example:**

For the first step, you would do:

```
    x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1);
```

## Code - The easy one

```py
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        # approach 1
        bin_A = bin(A)[2:]
        # print(bin_A)
        n = len(bin_A)
        bin_A = '0'*(32-n) + bin_A
        return int(bin_A[::-1], 2)
```

## Code - The other one

```py
# approach 2
bin_A = bin(A)[2:]
n = len(bin_A)
bin_A = '0'*(32-n) + bin_A
bin_A = list(bin_A)
for i in range(16):
    if int(bin_A[i]) ^ int(bin_A[31-i]) > 0:
        bin_A[i], bin_A[31-i] = bin_A[31-i], bin_A[i]
return int(''.join(bin_A), 2)
```
