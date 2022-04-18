import sys
import itertools as itr

word, result = sys.stdin.readline().strip(), []
for c in itr.combinations(range(1, len(word)), 2):
    word1, word2, word3 = word[:c[0]], word[c[0]:c[1]], word[c[1]:]
    new_word = word1[::-1] + word2[::-1] + word3[::-1]
    result.append(new_word)
result.sort()
print(result[0])