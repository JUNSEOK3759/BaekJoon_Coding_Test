import sys
import re
from collections import deque, Counter
import heapq as hq
import copy
import math
import itertools
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

from collections import deque
month, day, year, time = map(str, input().rstrip().split())
year = int(year)

mon = {'January' : 31,
       'February' : 29 if int(year) % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28,
       'March' : 31,
       'April' : 30,
       'May' : 31,
       'June' : 30,
       'July' : 31,
       'August' : 31,
       'September' : 30,
       'October' : 31,
       'November' : 30,
       'December' : 31}



day = re.sub(',', '', day)
day = int(day)
hour, min = time.split(':')
hour, min = int(hour), int(min)
dayCount = 0
for i in mon.values():
    dayCount += i
all = 60*60*24 * dayCount

fuck = 0
for i, x in mon.items():
    if i == month:
        break
    fuck += x


qwe = (min*60) + (hour*60*60) + ((day+fuck-1) * 24 * 60 * 60)


print(qwe/all * 100)

