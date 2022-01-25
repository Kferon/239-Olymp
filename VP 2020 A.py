n = int(input())
mas = list(map(int, input().split()))
num = 0
check = 0
ans = []
for i in range(n):
    if mas[i] % 2 == 1:
        num += 1

if num % 2 == 1:
    for j in  range(n-1):
        ans.append('+')
else:
    for j in range (n-1):
        if check != 1:
            if mas[j] % 2 == 1:
                ans.append('x')
                check = 1
            else:
                ans.append('+')
        else:
            ans.append('+')

for i in ans:
    print(i, end='')