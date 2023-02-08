def solution(numbers, target):
    head = [0]
    for i in numbers:
        heap = []
        for j in head:
            heap.append(j+i)
            heap.append(j-i)
        head = heap
    return head.count(target)