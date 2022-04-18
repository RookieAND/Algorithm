count = int(input())
result = count
for _ in range(0, count):
    word = input()
    for index in range(0, len(word) - 1):
        # 두 문자가 연이어 같이 들어오면, 구문을 pass 시킴
        if word[index] == word[index+1]:
            continue
        # 해당 문자가 연달아 들어오지 않고, 그 이후의 문자열에 포함되어 있다면 안됨.
        elif word[index] in word[index+1:]:
            result -= 1
            break
print(result)
