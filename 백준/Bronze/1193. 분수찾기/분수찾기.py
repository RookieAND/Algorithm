floor, cell, x = 1, 1, int(input())

while True:
    if x > cell:
        floor += 1
        cell += floor
    else:
        behind_cell = sum(range(1, floor))
        if floor % 2 == 0:
            print(f"{x - behind_cell}/{floor - (x - behind_cell - 1)}")
        else:
            print(f"{floor - (x - behind_cell - 1)}/{x - behind_cell}")
        break