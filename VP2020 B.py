n = int(input())
k = int(input())
a = sorted(list(map(int, input().split())))
x, y, min_p, max_p = 0, 0, 1, 1
for i in range(1, k):
    if a[x] < i:
        x += 1
    else:
        min_p += 1
    while y < n - 1 and a[y] < i:
        y += 1
    if y < n - 1:
        y += 1
        max_p += 1
print(min_p)
print(max_p)