a = str(input())

cnt = 0

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        cnt += 1

print((cnt + 1) // 2)