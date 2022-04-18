word = input()
list(map(lambda x: print(word.find(chr(x)), end=" "), range(0x61, 0x7B)))