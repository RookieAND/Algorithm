import sys

S = sys.stdin.readline().rstrip()
result, word = "", ""


def append_word(result, word):
    word_list = word.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i][::-1]
    result += " ".join(word_list)
    return result


is_tag = False
for char in S:
    if char == '<':
        is_tag = True
        if word:
            result = append_word(result, word)
            word = ""
            result += char
        else:
            result += char
        continue
    if char == '>':
        is_tag = False
        result += char
        continue

    if is_tag:
        result += char
    else:
        word += char

if word:
    result = append_word(result, word)

print(result)