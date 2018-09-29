def countNoOfReferences(arr, num, search_first=True):
    n = len(arr)
    res = -1
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            res = mid
            if search_first:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return res


arr = [1, 1, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 5]
num = 2
first = countNoOfReferences(arr, num, True)
if first != -1:
    last = countNoOfReferences(arr, num, False)
    print(last - first + 1)
else:
    print(-1)
