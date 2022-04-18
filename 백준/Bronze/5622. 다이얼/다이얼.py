word, dialog = input(), '22233344455566677778889999'
print(sum(map(lambda char: int(dialog[ord(char) - ord('A')]), word)) + len(word))