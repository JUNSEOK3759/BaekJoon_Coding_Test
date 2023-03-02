def solution(numbers, hand):
    answer = ''
    pad = {'1' : [0, 0], '2' : [0, 1], '3' : [0, 2],
           '4' : [1, 0], '5' : [1, 1], '6' : [1, 2],
           '7' : [2, 0], '8' : [2, 1], '9' : [2, 2],
           '*' : [3, 0], '0' : [3, 1], '#' : [3, 2]
          }
    left = pad['*']
    right = pad['#']
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = pad[str(i)]
        elif i in [3, 6, 9]:
            answer += 'R'
            right = pad[str(i)]
        else:
            left_dis = abs(pad[str(i)][0] - left[0]) + abs(pad[str(i)][1] - left[1])
            right_dis = abs(pad[str(i)][0] - right[0]) + abs(pad[str(i)][1] - right[1])
            if left_dis < right_dis:
                answer += 'L'
                left = pad[str(i)]
            elif left_dis > right_dis:
                answer += 'R'
                right = pad[str(i)]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = pad[str(i)]
                else:
                    answer += 'R'
                    right = pad[str(i)]
    return answer