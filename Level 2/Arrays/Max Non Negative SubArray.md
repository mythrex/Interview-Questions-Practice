# Max Non Negative SubArray

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

**Example:**

```
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
```

**NOTE:** If there is a tie, then compare with segment's length and return segment which has maximum length
**NOTE 2:** If there is still a tie, then return the segment with minimum starting index

## Solution Approach

```
Loop i = 1 to Array.length :
        IF current element is positive :
                update current sum
                compare max sum with current sum
                update max sum
                update max ranges
        ELSE :
            current sum := 0
            update current ranges.
EndLoop;

return elements of max ranges
```

## Code

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        maxSumList = []
        curSumList = []
        cursum = 0
        maxsum = 0
        for i in A:
            if i >= 0:
                cursum += i
                curSumList.append(i)
                if cursum > maxsum:
                    maxsum = cursum
                    maxSumList = curSumList
                elif cursum == maxsum:
                    if len(curSumList) > len(maxSumList):
                        maxSumList = curSumList
            else:
                cursum = 0
                curSumList = []
            # print(i)
        return maxSumList
```
