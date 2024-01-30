def getting_mad(arr):
    arr = sorted(arr)

    l = arr[0]
    mad = abs(l - arr[-1])

    for i in arr[1:]:
        diff = abs(l - i)
        l = i
        if diff < mad: mad = diff
        if not diff: break

    return mad

print(getting_mad([4, 2, 6, 8, 13, 5, 6]))