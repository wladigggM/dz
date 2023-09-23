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
    # insert_data(sales_list, 3)

    open_file('c.txt', customers_list)
    # insert_data(customers_list, 4)

    # - - - - - - - - - - - - - - - - - - - - - ОТЛАДОЧНЫЙ ИНТЕРФЕЙС - - - - - - - - - - - - - - - - - - - - - - - - #

    while True:
        choice = int(input("""
        Кто вы ?
        1. Продавец
        2. Заказчик
        """))

        # - - - - - - - - - - - - - - - - - - - - - - ПРОДАВЕЦ - - - - - - - - - - - - - - - - - - - - - - - - - #

        if choice == 1:
            choice = int(input("""
            1. зарегистрировать нового продавца
            2. отредактировать продавца
            3. удалить продавца
            """))
            if choice == 1:
                count = 0
                sales_data = []
                print("""Введите поочередно:
                ИМЯ/ГОРОД/КОММИСИОННЫЕ
                """)
                while count != 3:
                    inp = input('>')
                    sales_data.append(tuple(inp.split(' ')))
                    count += 1
                cur.execute("""
                INSERT INTO salespeople (sname,city,comm) VALUES (?,?,?)""",
                            (sales_data[0][0], sales_data[1][0], sales_data[2][0]))
                break
            elif choice == 2:
                count = 0
                sales_up_data = []
                id_inp = int(input("""Введите id продавца которого  нужно отредактировать.
                """))
                print("""Введите поочередно:
                ИМЯ/ГОРОД/КОММИСИОННЫЕ
                """)
                while count != 3:
                    inp = input('>')
                    sales_up_data.append(tuple(inp.split(' ')))
                    count += 1
                cur.execute(f"""
                UPDATE salespeople 
                SET sname = '{sales_up_data[0][0]}', city = '{sales_up_data[1][0]}', comm = {sales_up_data[2][0]}
                WHERE id = {id_inp}""", )
                break
            elif choice == 3:
                inp = input("""
                Введите id продавца которого нужно удалить.
                """)

                cur.execute(f"""
                DELETE FROM salespeople WHERE id = '{inp}'
                """)
                break

        # - - - - - - - - - - - - - - - - - - - - - - ЗАКАЗЧИК - - - - - - - - - - - - - - - - - - - - - - - - - #

        elif choice == 2:
            choice = int(input("""
            1. зарегистрировать нового заказчика
            2. отредактировать заказчика
            3. удалить заказчика
            """))
            if choice == 1:
                count = 0
                sales_data = []
                print("""Введите поочередно:
                ИМЯ/ГОРОД/РЕЙТИНГ/ID_ЗАКРЕПЛЕННОГО_ПРОДАВЦА
                """)
                while count != 4:
                    inp = input('>')
                    sales_data.append(tuple(inp.split(' ')))
                    count += 1
                cur.execute("""
                INSERT INTO customers (cname,city,rating,id_sp) VALUES (?,?,?,?)""",
                            (sales_data[0][0], sales_data[1][0], sales_data[2][0], sales_data[3][0]))
                break
            elif choice == 2:
                count = 0
                sales_up_data = []
                id_inp = int(input("""Введите id заказчика которого  нужно отредактировать.
                """))
                print("""Введите поочередно:
                ИМЯ/ГОРОД/РЕЙТИНГ/ID_ЗАКРЕПЛЕННОГО_ПРОДАВЦА
                """)
                while count != 4:
                    inp = input('>')
                    sales_up_data.append(tuple(inp.split(' ')))
                    count += 1
                cur.execute(f"""
                UPDATE customers 
                SET cname = '{sales_up_data[0][0]}', city = '{sales_up_data[1][0]}', rating = {sales_up_data[2][0]}, id_sp = '{sales_up_data[3][0]}'
                WHERE id = {id_inp}""", )
                break
            elif choice == 3:
                inp = input("""
                Введите id заказчика которого нужно удалить.
                """)

                cur.execute(f"""
                DELETE FROM customers WHERE id = '{inp}'
                """)
                break
