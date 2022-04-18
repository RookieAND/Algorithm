play, ascend = list(map(int, input().split())), list(range(1, 9))
if play == ascend:
    print("ascending")
elif play == ascend[::-1]:
    print("descending")
else:
    print("mixed")