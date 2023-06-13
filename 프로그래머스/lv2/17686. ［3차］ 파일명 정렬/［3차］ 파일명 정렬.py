from collections import deque
def solution(files):
    answer = []
    x = []
    for i in range(len(files)):
        h, n, t = '', '', ''
        cnt = 0
        while not files[i][cnt].isdigit():
            h += files[i][cnt]
            cnt += 1
        for j in range(cnt, len(files[i])):
            if not files[i][j].isdigit():
                n = files[i][cnt : j]
                cnt = j
                t = files[i][j:]
                break
        else:
            n = files[i][cnt:]    
        
        x.append([h, n, t])
        
            
    x.sort(key = lambda x : (x[0].lower(), int(x[1])))
    for i in x:
        answer.append(''.join(i))
    return answer