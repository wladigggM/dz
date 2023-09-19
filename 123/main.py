import sqlite3 as sql

with sql.connect('newDB.db') as connect:
    cur = connect.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS computers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        brand TEXT NOT NULL,
        price INTEGER NOT NULL);
    """)

    # cur.execute("""
    # INSERT INTO computers (type, brand, price) VALUES
    #     ('ноутбук','hp',10000),
    #     ('стационарный компьютер','hp',20000),
    #     ('моноблок','hp',15000),
    #     ('стационарный компьютер','msi',50000),
    #     ('ноутбук','asus', 30500);
    #     """)

    res = cur.execute("""
    -- SELECT * FROM computers WHERE brand = 'hp';
    -- SELECT * FROM computers WHERE price > 40000;
    SELECT * FROM computers WHERE type = 'ноутбук' AND price < 30000;
    """)

    print(res.fetchall())
