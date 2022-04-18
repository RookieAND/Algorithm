croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sentence, count = input(), 0

for char in croatia:
    sentence = sentence.replace(char, '*')
print(len(sentence))