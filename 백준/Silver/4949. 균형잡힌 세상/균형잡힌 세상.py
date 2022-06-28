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
            # 만약 더 이상 필요한 닫힌 괄호가 없다면, False 리턴.
            if len(needed_bracket) == 0:
                return False
            # 만약 필요한 닫힌 괄호가 나오지 않았다면, False 리턴
            needed = needed_bracket.pop()
            if needed != char:
                return False
    # 남는 괄호 (닫히지 않은 괄호) 가 있다면, False 리턴
    if len(needed_bracket) > 0:
        return False
    return True


while True:
    # 마지막 개행문자만을 제거하기 위해 rstrip 함수 사용.
    sentence = sys.stdin.readline().rstrip()
    # 종료 조건을 파악하기 위한 조건문
    if sentence == '.':
        break
    result = check_sentence(sentence)
    print('yes' if result else 'no')
