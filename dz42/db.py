import sqlite3 as sql


def create_account_table():
    try:
        with sql.connect('accounts.db') as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency TEXT,
            score INTEGER,
            id_user INTEGER,
            FOREIGN KEY (id_user) REFERENCES users (id)
            )""")

            cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            user_lastname TEXT,
            mail_code TEXT
            )""")
    except sql.Error as err:
        print(err)


def create_account(user_name, user_lastname, mail_code):
    with sql.connect('accounts.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO users (user_name, user_lastname, mail_code) VALUES (?,?,?)""",
                    (user_name, user_lastname, mail_code))


def open_account(user_name, user_lastname, type_currency):
    with sql.connect('accounts.db') as conn:
        cur = conn.cursor()
        id_sercher = cur.execute("""SELECT id FROM users WHERE user_name =? and user_lastname =?""",
                                 (user_name, user_lastname))
        for id in id_sercher.fetchall():
            if type_currency == 'Dollar':
                cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Dollar', 0,?)""", id)
            elif type_currency == 'Pound':
                cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Pound', 0,?)""", id)
            elif type_currency == 'Rupee':
                cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Rupee',0,?)""", id)
            else:
                print('Неизвестный тип счета')


def view_accounts():
    with sql.connect('accounts.db') as conn:
        cur = conn.cursor()
        all_users = cur.execute("""SELECT * FROM users""")
        print(all_users.fetchall())
