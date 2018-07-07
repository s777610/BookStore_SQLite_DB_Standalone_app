import sqlite3

def connect():
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))  # NULL is id
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# the id will be extracted from tuple,
# the tuple will have ID as the first item
def delete(id):
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()



connect()
# insert("The earth", "boyboy", 1993, 4484384)
# update(4, "The earth!!", "John Smooth", 1917, 78767698)
# print(view())
# delete(2)
# print(search(author="boyboy"))
