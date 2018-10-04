def distinctCharSubString(S):
    n = len(S)
    # len of distinct Characters
    dist = len(set(S))
    curr_count = dict(zip('abcdefghijklmnopqrstuvwxyz', [0]*26))
    min_len = float('inf')
    start = 0
    cur_dist_count = 0
    for i in range(n):
        curr_count[S[i]] += 1
        # if distinct char
        if curr_count[S[i]] == 1:
            cur_dist_count += 1
        # if found all the distinct chars
        if cur_dist_count == dist:
            # if first letter of window count > 1
            # minimize window
            while curr_count[S[start]] > 1:
                curr_count[S[start]] -= 1
                start += 1
            win_len = i - start + 1
            min_len = min(min_len, win_len)
    return S[start:start+min_len]


res = distinctCharSubString('aabbccaaa')
print(res)
