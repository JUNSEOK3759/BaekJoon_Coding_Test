def makeBinary(x):
    k = ''
    while x:
        k += str(x % 2)
        x = x // 2
    return k[::-1]

def solution(s):
    answer = [0, 0]
    while s != '1':
        be_s = len(s)
        s = ''.join(s.split('0'))
        af_s = len(s)
        s = makeBinary(af_s)
        answer[0] += 1
        answer[1] += (be_s - af_s)
    return answer