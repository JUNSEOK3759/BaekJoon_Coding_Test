def solution(files):
    name = []
    
    for x in files:
        a, b, c = '','',''
        qw = 0
        for j in range(len(x)):
            if x[j].isdigit():
                a = x[:j]
                qw = j
                break
        for k in range(qw, len(x)):
            
            if not x[k].isdigit():
                b = x[qw:k]
                c = x[k:]
                break
        else:
            b = x[qw:]       
        name.append([a, b, c])
    name.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for i in range(len(name)):
        name[i] = ''.join(name[i]) 
    return name