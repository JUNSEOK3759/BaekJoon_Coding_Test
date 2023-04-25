n = int(input())

dis = list(map(int, input().split()))

oil = list(map(int, input().split()))
oil.pop()

disSum = sum(dis)

sum = 0
for i in range(len(oil)-1):
    if oil[i] != min(oil):
        sum += oil[i] * dis[i]
        disSum -= dis[i]
    else:
        sum += oil[i] * disSum
        disSum = 0
        break

print(sum)