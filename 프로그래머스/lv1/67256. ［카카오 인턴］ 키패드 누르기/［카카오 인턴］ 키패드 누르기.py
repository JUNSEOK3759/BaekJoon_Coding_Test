def solution(numbers, hand):
    answer = ''
    pad = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
           4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
           7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
           '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]}
    left, right = '*', '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            left_dis = abs(pad[left][0] - pad[num][0]) + abs(pad[left][1] - pad[num][1])
            right_dis = abs(pad[right][0] - pad[num][0]) + abs(pad[right][1] - pad[num][1])
            
            if left_dis > right_dis:
                answer += 'R'
                right = num
            elif left_dis < right_dis:
                answer += 'L'
                left = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    return answer