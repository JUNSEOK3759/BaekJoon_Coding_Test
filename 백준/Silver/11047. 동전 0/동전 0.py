n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))
    
a.sort(reverse = True)

i = 0
sum = 0
while m > 0:
    if a[i] > m:
        i += 1
    else:
        sum += m // a[i]
        m = m % a[i]

print(sum)