def is_multiple_3(num: str, count: int):
    if len(num) == 1:
        print(count)
        if num in ['3', '6', '9']:
            print("YES")
        else:
            print("NO")
        return
    else:
        count += 1
        result = sum(map(int, num))
        is_multiple_3(str(result), count)


is_multiple_3(input(), 0)