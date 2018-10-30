# Hotel Bookings Possible

A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

```
Input:

First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.



Output:
A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.


Example :
Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0

At day = 5, there are 2 guests in the hotel. But I have only one room.
```

## My Solution Approach

1 3 5
2 6 8

My solution works as follows
Start with 1 till 8

```
Check if
With departure. If D < n and derpart[D] ==  i
K++
if(D < n and depart[D] == i):
                D += 1
                K += 1
            if(A < n and arrive[A] == i):
                if K > 0:
                    K -= 1
                else:
                    return 0
                A +=1
```

## My Code

```py
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive = sorted(arrive)
        depart = sorted(depart)
        n = len(arrive)
        start = arrive[0]
        end = depart[n - 1]
        A = 0
        D = 0
        rooms = 0
        for i in range(start, end + 1):
            if(D < n and depart[D] == i):
                D += 1
                K += 1
            if(A < n and arrive[A] == i):
                if K > 0:
                    K -= 1
                else:
                    return 0
                A +=1
        return 1
```

`But for some reason my code gives time limit error`

## The editorial Code

1. Create event points for every interval start, and end.
2. Sort it according to the day.
3. Now, iterate over them one by one. If you encounter a start, then the number of active guests increase by one. If you encounter an end, the number of active guests decrease by one.
4. If at any point, the number of active guests exceed K, we know that scheduling is not possible.

## The Editorial Code

```py
class Solution:
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1
```
