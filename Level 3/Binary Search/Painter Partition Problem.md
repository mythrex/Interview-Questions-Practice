# Painter's Partition Problem

Asked in: **Google**

You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

1. 2 painters cannot share a board to paint. That is to say,
   a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. Which means a
   configuration where painter 1 paints board 1 and 3 but not 2 is
   invalid.

`Return the ans % 10000003`

**Example**

```
Input :
  K : 2
  T : 5
  L : [1, 10]

Output : 50
```

## Hint

Hint : Think binary search for the answer.

If you had a function bool isPossible which could tell you if its possible to paint the boards in time T or less, can you solve the problem ?

```python
def isPossible(time, l, k):
    # l: list
    # k: total no of painters
    painter = 1
    time_taken = 0
    if maxi > time:
        return False
    for i in l:
        time_taken += i
        if time_taken > time:
            painter += 1
            time_taken = i
        # print(time_taken, painter)
        if painter > k:
            return False
    return True
```

## Solution Approach

If you have already solved the problem corresponding to hint1, you are already halfway there.

You can do a binary search for the answer :

```
start = 0, end = max_time_possible
  mid = (start + end) / 2
  if isPossible(mid):
  	end = mid - 1
  else
	start = mid + 1
```

Now, lets look into how isPossible would be implemented.
Keep assigning boards to painter greedily till the time taken < mid. If you run out of painters, isPossible = false.
else isPossible = true.

## Code

```python
def isPossible(time, l, k):
    painter = 1
    time_taken = 0
    if maxi > time:
        return False
    for i in l:
        time_taken += i
        if time_taken > time:
            painter += 1
            time_taken = i
        # print(time_taken, painter)
        if painter > k:
            return False
    return True

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        low, high = 0, sum(C)
        sol = float('inf')
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid)
            if isPossible(mid, C, A):
                high = mid - 1
                sol = min(sol, mid)
            else:
                low = mid + 1
        return (sol*B) % 10000003
<<<<<<< HEAD
=======

>>>>>>> 2fb8a34698c21a19f21e8d7765ade0e9cf1dce11
```
