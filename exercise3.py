"""
The goal of this exercise is to assess SQL skills.

The init() function creates a SQLite database.

Please read the comments after it and answer the 3 questions.
"""

import sqlite3


def init(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS countries")
    c.execute("CREATE TABLE countries ("
              "id INTEGER PRIMARY KEY, "
              "code TEXT, "
              "name TEXT)")
    c.execute("INSERT INTO countries VALUES (1, 'US', 'United States')")
    c.execute("INSERT INTO countries VALUES (2, 'MX', 'Mexico')")
    c.execute("INSERT INTO countries VALUES (3, 'CA', 'Canada')")
    c.execute("INSERT INTO countries VALUES (4, 'BR', 'Brazil')")
    c.execute("INSERT INTO countries VALUES (5, 'CU', 'Cuba')")

    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users ("
              "id INTEGER PRIMARY KEY, "
              "name TEXT, "
              "country_id INTEGER, "
              "FOREIGN KEY(country_id) REFERENCES countries(id))")
    c.execute("INSERT INTO users VALUES (1, 'Jenci Anshel', 1)")
    c.execute("INSERT INTO users VALUES (2, 'Jory Divina', 2)")
    c.execute("INSERT INTO users VALUES (3, 'Mateo Heidi', 2)")
    c.execute("INSERT INTO users VALUES (4, 'Éimhear Sigmund', 2)")
    c.execute("INSERT INTO users VALUES (5, 'Monat Heracles', 3)")
    c.execute("INSERT INTO users VALUES (6, 'Feodor Amalbert', 3)")
    c.execute("INSERT INTO users VALUES (7, 'Mahpiya Vartolomej', 1)")
    c.execute("INSERT INTO users VALUES (8, 'Mirta Ankur', 1)")
    c.execute("INSERT INTO users VALUES (9, 'Shankar Darío', 1)")
    c.execute("INSERT INTO users VALUES (10, 'Hanna Ibrahim', 2)")
    c.execute("INSERT INTO users VALUES (11, 'Reyna Rajeev', 4)")
    c.execute("INSERT INTO users VALUES (12, 'Roshanara Hallbjörn', 2)")

    c.execute("DROP TABLE IF EXISTS items")
    c.execute("CREATE TABLE items ("
              "id INTEGER PRIMARY KEY, "
              "sku TEXT, "
              "name TEXT)")
    c.execute("INSERT INTO items VALUES (1, 'jeab', 'Jeans - black')")
    c.execute("INSERT INTO items VALUES (2, 'jeap', 'Jeans - pink')")
    c.execute("INSERT INTO items VALUES (3, 'shor', 'Shoes - red')")
    c.execute("INSERT INTO items VALUES (4, 'shoy', 'Shoes - yellow')")
    c.execute("INSERT INTO items VALUES (5, 'shio', 'Shirt - orange')")
    c.execute("INSERT INTO items VALUES (6, 'shib', 'Shirt - blue')")

    c.execute("DROP TABLE IF EXISTS orders")
    c.execute("CREATE TABLE orders ("
              "id INTEGER PRIMARY KEY, "
              "user_id INTEGER, "
              "item_id INTEGER, "
              "datetime STRING, "
              "FOREIGN KEY(user_id) REFERENCES users(id), "
              "FOREIGN KEY(item_id) REFERENCES items(id))")
    c.execute("INSERT INTO orders VALUES (1, 1, 1, '2017-01-02 11:34:59')")
    c.execute("INSERT INTO orders VALUES (2, 1, 3, '2017-01-09 18:02:06')")
    c.execute("INSERT INTO orders VALUES (3, 1, 5, '2017-01-14 21:38:19')")
    c.execute("INSERT INTO orders VALUES (4, 2, 1, '2017-03-10 05:47:31')")
    c.execute("INSERT INTO orders VALUES (5, 2, 1, '2017-05-20 03:19:46')")
    c.execute("INSERT INTO orders VALUES (6, 2, 4, '2017-06-20 24:51:47')")
    c.execute("INSERT INTO orders VALUES (7, 2, 4, '2017-07-12 22:31:40')")
    c.execute("INSERT INTO orders VALUES (8, 2, 5, '2017-07-28 20:43:43')")
    c.execute("INSERT INTO orders VALUES (9, 4, 2, '2017-08-26 04:43:14')")
    c.execute("INSERT INTO orders VALUES (10, 4, 1, '2017-09-12 16:48:41')")
    c.execute("INSERT INTO orders VALUES (11, 4, 2, '2017-09-22 02:58:21')")
    c.execute("INSERT INTO orders VALUES (12, 7, 5, '2017-10-12 22:31:40')")
    c.execute("INSERT INTO orders VALUES (13, 7, 6, '2017-10-21 12:55:56')")
    c.execute("INSERT INTO orders VALUES (14, 9, 2, '2017-10-29 21:52:58')")
    c.execute("INSERT INTO orders VALUES (15, 9, 4, '2017-11-12 16:48:41')")
    c.execute("INSERT INTO orders VALUES (16, 9, 6, '2017-11-21 07:15:24')")
    c.execute("INSERT INTO orders VALUES (17, 9, 4, '2017-12-26 04:43:14')")

    conn.commit()


def query_users_from_mx_with_black_jeans(conn):
    """
    1. Modify the following query to return the list of names of Mexican users having bought black jeans
    """
    c = conn.cursor()
    c.execute("""

    SELECT 1

    """)
    return c.fetchall()


def query_users_who_bought_nothing(conn):
    """
    2. Modify the following query to return the name and country of users who bought nothing
    """
    c = conn.cursor()
    c.execute("""

    SELECT 1

    """)
    return c.fetchall()


# 3. Finally, imagine you have millions of users, items and orders,
# add code to the init() function to create database indexes that could optimize your queries.
# Add comments explaining your choices

if __name__ == '__main__':
    conn = sqlite3.connect('store.db')
    init(conn)
    print(query_users_from_mx_with_black_jeans(conn))
    print(query_users_who_bought_nothing(conn))
    conn.close()
