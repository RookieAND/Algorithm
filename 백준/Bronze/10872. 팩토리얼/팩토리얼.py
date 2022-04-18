def factorial(num: int):
    result = 1
    if num > 0:
        result = num * factorial(num - 1)
    return result


print(factorial(int(input())))