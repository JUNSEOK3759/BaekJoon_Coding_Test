n = int(input())

a = list(map(int, input().split()))
a.sort()

res = 0
for i in range(len(a)):
    res += sum(a[0 : i+1])
print(res)