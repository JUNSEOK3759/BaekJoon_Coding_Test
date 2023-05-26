def solution(storey):
    answer = 0
    
    while storey:
        x = storey % 10
        
        if x > 5:
            answer += (10 - x)
            storey += 10
        elif x < 5:
            answer += x
        
        else:       
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += x
        storey //= 10
    return answer