def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = s
    for word in words:
        if word in result:
            result = result.replace(word, str(words.index(word)))
    return int(result)