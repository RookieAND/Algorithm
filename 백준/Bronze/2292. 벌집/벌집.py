num, floor, ceil = int(input()), 1, 1
while num > ceil:
    ceil += 6 * floor
    floor += 1
print(floor)