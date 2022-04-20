import sys

# 먼저 해당 수식을 -를 기준으로 분할하여 새로운 list를 만든다.
# 수식에 마이너스가 왔다면, 다음 마이너스가 오기 전까지 모든 값을 더해주고 이를 제하면 된다.
# 예시 : 55-50+45-33+27 -> 55 - (50 + 45) - (33 + 27) 로 변경이 가능하다.
expression = sys.stdin.readline().strip().split('-')
for i in range(len(expression)):
    sumNum = 0
    for num in expression[i].split('+'):
        sumNum += int(num)
    # 수식의 가장 첫번째 파트라면, 합산한 결과를 더한다.
    if i == 0:
        result = sumNum
    # 그렇지 않으면, 합산한 결과를 빼준다.
    else:
        result -= sumNum
print(result)