# 균형잡힌 문자열이 아닌 케이스

# 1. 열린 괄호와 닫힌 괄호의 수량이 다른 경우. ((()), [(]
# 2. 바깥 쪽의 괄호보다 안쪽의 괄호가 더 나중에 닫혔을 경우. ([ )]
# ([ (([( [ ] ) ( ) (( ))] )) ]) => [), ], ), ), ], ),

import sys

bracket = {'(': ')', '[': ']'}


def check_sentence(stc):
    needed_bracket = []
    for char in stc:
        # 열린 괄호가 추가되었다면, 필요한 닫힌 괄호를 순차적으로 추가
        if char == '(' or char == '[':
            needed_bracket.append(bracket[char])
            continue
        if char == ')' or char == ']':
            # 리스트가 비었거나 필요한 닫힌 괄호가 나오지 않았다면, False.
            if not needed_bracket or needed_bracket[-1] != char:
                return False
            # 상단의 결격 사유가 없을 경우, 리스트에서 필요한 괄호를 제거.
            needed_bracket.pop()
    # 남는 괄호 (닫히지 않은 괄호) 가 있다면, False 리턴
    if needed_bracket:
        return False
    return True


while True:
    # 마지막 개행문자만을 제거하기 위해 rstrip 함수 사용.
    sentence = sys.stdin.readline().rstrip()
    # 종료 조건을 파악하기 위한 조건문
    if sentence == '.':
        break
    print('yes' if check_sentence(sentence) else 'no')
