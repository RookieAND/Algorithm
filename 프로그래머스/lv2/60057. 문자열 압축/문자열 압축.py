def solution(s):
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):
        shorten = ""
        current, amount = s[0:length], 1
        for i in range(length, len(s) + 1, length):
            word = s[i:i+length]
            if current == word:
                amount += 1
            else:
                shorten += f"{amount}{current}" if amount > 1 else current
                current, amount = word, 1
        shorten += current
        answer = min(answer, len(shorten))
    return answer