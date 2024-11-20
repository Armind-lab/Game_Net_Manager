import sqlite3

def add_to_database(n , s , p , sr):
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (name , system , player , start_time) VALUES (? , ? , ? , ?)" , (n , s , p , sr))

    connection.commit()
    connection.close()

def price_info():
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM price")

    res = cursor.fetchone()

    connection.commit()
    connection.close()

    return res

def add_price(ps41, ps42, ps43, ps44, ps51, ps52, ps53, ps54):
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE price SET PS41=?, PS42=?, PS43=?, PS44=?, PS51=?, PS52=?, PS53=?, PS54=?", (ps41, ps42, ps43, ps44, ps51, ps52, ps53, ps54))

    connection.commit()
    connection.close()

def user_info():
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    res = cursor.fetchall()

    connection.commit()
    connection.close()

    return res

def delete_user(user):
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE name = ?", (user,))

    connection.commit()
    connection.close()

def empty():
    connection = sqlite3.connect('./database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM price")

    row = cursor.fetchone()[0]

    connection.commit()
    connection.close()

    return row == 0

connection = sqlite3.connect('./database.db')
cursor = connection.cursor()

# sql1 = """
#     DROP TABLE users;
# """

# sql2 = """
#     DROP TABLE price;
# """

sql1 = """
    CREATE TABLE IF NOT EXISTS users(
    name TEXT NOT NULL,
    system TEXT NOT NULL,
    player TEXT NOT NULL,
    start_time TIME);
"""

sql2 = """
    CREATE TABLE IF NOT EXISTS price(
    PS41 INTEGER,
    PS42 INTEGER,
    PS43 INTEGER,
    PS44 INTEGER,
    PS51 INTEGER,
    PS52 INTEGER,
    PS53 INTEGER,
    PS54 INTEGER);
"""

cursor.execute(sql1)
cursor.execute(sql2)

if empty():
    cursor.execute("INSERT INTO price values(0, 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO users (name , system , player) VALUES ('نام' , 'سیستم' , 'تعداد')")

cursor.execute(sql1)

connection.commit()
connection.close()