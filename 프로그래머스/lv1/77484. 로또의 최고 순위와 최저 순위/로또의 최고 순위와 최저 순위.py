# 최대 당첨 숫자의 수량 : (기존에 맞춘 숫자) + 0의 갯수
# 최소 당첨 숫자의 수량 : (기존에 맞춘 숫자)

# 1~5등까지는 7 - (당첨 숫자 수량) 으로 순위가 도출됨
# 6등만 당첨 숫자 수량이 2 미만일 때 적용

def solution(lottos, win_nums):
    correct = 0
    zeroCount = lottos.count(0)
    for num in range(6):
        if win_nums[num] in lottos:
            correct += 1
    if correct + zeroCount < 2:
        answer = [6, 6] 
    else:
        if correct < 2:
            answer = [7 - correct - zeroCount, 6]
        else:
            answer = [7 - correct - zeroCount, 7 - correct]

    return answer
    
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [1, 4, 17, 5, 33, 14]
print(solution(lottos, win_nums))