count, strList = int(input()), []
for i in range(0, count):
    tCount, tString = input().split()
    string = ""
    for char in tString:
        string += char * int(tCount)
    strList.append(string)
list(map(lambda x: print(x), strList))