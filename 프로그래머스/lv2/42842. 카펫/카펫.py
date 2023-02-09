def solution(brown, yellow):
    width_height = (brown + 4) // 2
    for num in range(1, (width_height // 2) + 1):
        print(num, width_height - num, num * (width_height - num))
        if num * (width_height - num) == brown + yellow:
            return [width_height - num, num]