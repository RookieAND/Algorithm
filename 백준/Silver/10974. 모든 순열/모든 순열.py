import sys
import itertools as itr

n, data = int(sys.stdin.readline()), []
for c in itr.permutations(range(1, n+1), n):
    data.append(c)
for num in data:
    string = ""
    for i in range(n):
        string += str(num[i]) + " "
    print(string)