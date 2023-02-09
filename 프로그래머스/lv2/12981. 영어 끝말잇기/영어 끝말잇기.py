def solution(n, words):
    prev_word = [words[0]]

    for idx in range(1, len(words)):
        current_word = words[idx]
        # 이전에 등장했던 단어를 다시 사용하거나, 앞 사람이 말한 단어의 마지막 문자로 시작하지 않았을 경우.
        if current_word in prev_word or current_word[0] != prev_word[-1][-1]:
            return [(idx % n) + 1, (idx // n) + 1]
        prev_word.append(current_word)
    return [0, 0]