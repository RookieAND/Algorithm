import sys

S = sys.stdin.readline().strip()
word_list = [S[i:] for i in range(len(S))]
word_list.sort()
print(*word_list, sep='\n')