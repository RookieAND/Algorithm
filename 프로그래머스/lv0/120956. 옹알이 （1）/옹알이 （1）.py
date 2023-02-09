def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        for cp in can_speak:
            if cp in word:
                word = word.replace(cp, '-')
        word = word.replace('-', '')
        answer += 1 if not len(word) else 0
        
    return answer