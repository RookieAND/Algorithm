word, frqChar, frqCount = input().upper(), '', 0
for char in set(word):
    if word.count(char) > frqCount:
        frqChar = char
        frqCount = word.count(char)
    elif word.count(char) == frqCount:
        frqChar = '?'
print(frqChar)