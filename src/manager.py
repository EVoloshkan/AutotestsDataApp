import csv
import json
from itertools import cycle

with open("../files/books.csv", newline='') as reader:
    data = csv.DictReader(reader)
    books = list(data)

with open("../files/users.json", "r") as reader:
    users = json.load(reader)

    user_books = []

    for user in users:
        new_user = dict(name=user['name'], gender=user['gender'], address=user['address'], age=user['age'], books=[])
        user_books.append(new_user)

    c_users = cycle(user_books)
    for book in books:
        current_user = next(c_users)
        new_book = dict(title=book['Title'], author=book['Author'], pages=book['Pages'], genre=book['Genre'])
        current_user['books'].append(new_book)

with open("../result/result.json", "w") as f:
    json.dump(user_books, f, indent=4)
