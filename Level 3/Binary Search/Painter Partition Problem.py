def isPossible(time, l, k):
    painter = 1
    time_taken = 0
    maxi = max(l)
    if maxi > time:
        return False
    for i in l:
        time_taken += i
        if time_taken > time:
            painter += 1
            time_taken = i
        print(time_taken, painter)
        if painter > k:
            return False
    return True


l = [6, 9, 3, 15, 12]
l1 = [3, 15, 6, 9, 12]
l3 = [5, 50]
time = 20
k = 2
print(isPossible(time, l3, k))
