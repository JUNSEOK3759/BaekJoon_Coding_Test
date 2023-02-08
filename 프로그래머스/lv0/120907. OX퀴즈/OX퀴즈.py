def solution(quiz):
        
    return ["O" if eval(i.replace('=', '==')) else "X"  for i in quiz]