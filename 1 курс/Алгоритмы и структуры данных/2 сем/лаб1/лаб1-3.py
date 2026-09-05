def deep(a, l, r):
    if l == r:
        return a[l:r+1]
    mid = (l + r) // 2
    left = deep(a, l, mid)
    right = deep(a, mid + 1, r)
    if left[-1] < right[0]:
        return max(left, right, left + right, key=len)
    return max(left, right, key=len)

a = list(map(int, input().split()))
sequence = deep(a, 0, len(a) - 1)
print(sequence)