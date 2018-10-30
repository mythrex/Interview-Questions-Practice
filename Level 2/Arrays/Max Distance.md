# Max Distance

Asked in **Google and Amazon**

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.

```
Example :
A : [3 5 4 2]

Output : 2
for the pair (3, 4)
```

## Solution Approach

Continuing from the previous hint :
It is important to note that while sorting the array we must also store the original index of the values instead of blindly sorting it.
Now iterate over every element in the sorted array as A[i].
Let us say index[i] stores the actual index of A[i].
Now, we are looking for all values of A[j] which are bigger than A[i].
Since the array is sorted, the values will be all the elements to the right of A[i].
Since we want to maximize index[j] - index[i], and index[i] is fixed,
we are essentially looking at max index[j] for all j > i.
The problem concludes to finding the max in all the suffix of the array.
We can preprocess the index array and let indexMax[i] store the maximum of index[i….len]
This is how we can calculate max of all the suffix in O(n) :

```
int maxIndex = INT_MIN; // -Infinity
for (int i = len - 1; i >= 0; i--) {
    maxIndex = max(maxIndex, index[i]);
    indexMax[i] = maxIndex;
}
```
