N, amount = int(input()), 0

while N >= 0:
    if N % 5 == 0:
        amount += N // 5
        print(amount)
        break
    else:
        amount +=1
        N -= 3
else:
    print(-1)