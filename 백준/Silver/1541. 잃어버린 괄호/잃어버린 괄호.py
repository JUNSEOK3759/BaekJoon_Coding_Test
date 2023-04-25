a = input().split('-')
res = []
for i in a:
    i = i.split('+')
    cnt = 0
    for j in i:
        cnt += int(j)
    res.append(cnt)
tot = res[0]
for i in range(1, len(res)):
    tot -= res[i]
    
print(tot)