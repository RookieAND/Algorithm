num, count = int(input()), 1
newNum = ((num % 10) * 10) + ((num // 10 + num % 10) % 10)
while num != newNum:
    count += 1
    newNum = ((newNum % 10) * 10) + ((newNum // 10 + newNum % 10) % 10)
print(count)