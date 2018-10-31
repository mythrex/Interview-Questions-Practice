# Maximum Consecutive Gap

_Fatt gyi thi solve krte krte_

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Example :

```
Input : [1, 10, 5]
Output : 5
```

Return 0 if the array contains less than 2 elements.

- You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
- You may also assume that the difference will not overflow.

## Solution Approach

A = [ 1, 5, 2, 3 9]
Output = 4

Now how to solve it

We need to make buckets of no and divide the no into it

Maximum gap can be when [1, 9]
I.e. when array has min and max elem only

Now minimum gap can only be when equally spaced elem are there in array.

[1, 3, 5, 7, 9]
Max_gap = 2

Our answer lies in [gap, Max - Min]
Where gap = Max - Min // n-1

So we make two buckets containing the following nos

        Min bucket


        Max bucket

[MIN, MIN + gap), [Min + gap, `MIN` + 2\* gap) ... and so on

There will only be (N-1) such buckets. We place the numbers in these buckets based on their value.
If you pick any 2 numbers from a single bucket, their difference will be less than gap, and hence they would never contribute to maxgap ( Remember maxgap >= gap ). We only need to store the largest number and the smallest number in each bucket, and we only look at the numbers across bucket.
Now, we just need to go through the bucket sequentially ( they are already sorted by value ), and get the difference of min_value with max_value of previous bucket with at least one value. We take maximum of all such values.

## Code

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n < 2:
            return 0
        MAX = -float('inf')
        MIN = float('inf')
        # O(n)
        min_i = min(A)
        max_i = max(A)
        # create buckets
        min_bucket = [MIN]*n
        max_bucket = [MAX]*n
        # calc gap
        gap = max((max_i - min_i) // (n-1), 1)
        # fill the buckets
        for x in A:
            i = min(n - 1, (x - min_i) // gap)
            min_bucket[i] = min(x, min_bucket[i])
            max_bucket[i] = max(x, max_bucket[i])
        # calc max gap
        max_gap = 0
        prev_gap = max_bucket[0]
        for i in range(1, n):
            if min_bucket[i] != MIN:
                max_gap = max(min_bucket[i] - prev_gap, max_gap)
                prev_gap = max_bucket[i]
        return max_gap
```
