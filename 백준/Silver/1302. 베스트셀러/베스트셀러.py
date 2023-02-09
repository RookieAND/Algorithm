import sys

read = sys.stdin.readline
books = {}
for _ in range(int(read())):
    book = read()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

most_selled = max(books.values())
most_sell_book = sorted([name for name in books.keys() if books[name] == most_selled])
print(most_sell_book[0])