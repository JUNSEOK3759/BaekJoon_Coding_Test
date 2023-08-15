def solution(nums):
    answer = 0
    len_n = len(nums) // 2
    x = set(nums)
    len_x = len(x)
    
    if len_x < len_n:
        return len_x
    else:
        return len_n
    