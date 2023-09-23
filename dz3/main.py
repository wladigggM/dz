import sqlite3 as sql


def open_file(file_name: str, empty_list: list):
    with open(f'{file_name}', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.split(',')
            empty_list.append(tuple(line))


def insert_data(insert_list: list, how_values: int):
    if how_values == 3:
        for el in insert_list:
            cur.execute("""
            INSERT INTO salespeople (sname,city,comm) VALUES(?,?,?)""", (el[0], el[1], el[2]))
    elif how_values == 4:
        for el in insert_list:
            cur.execute("""
            INSERT INTO customers (cname,city,rating,id_sp) VALUES(?,?,?,?)""", (el[0], el[1], el[2], el[3]))


with sql.connect('new.db') as conn:
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS salespeople(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sname TEXT NOT NULL,
        city TEXT NOT NULL,
        comm INTEGER
        );
        
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cname  TEXT NOT NULL,
        city TEXT NOT NULL,
        rating  INTEGER NOT NULL,
        id_sp INTEGER NOT NULL,
        FOREIGN KEY (id_sp) REFERENCES salespeople (id)
        );
    """)
    sales_list = []
    customers_list = []

    open_file('s.txt', sales_list)
    insert_data(sales_list, 3)

    open_file('c.txt', customers_list)
    insert_data(customers_list, 4)
