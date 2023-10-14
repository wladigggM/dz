import sqlite3 as sql


class User:
    def __init__(self, user_name, user_lastname, mail_code):
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.mail_code = mail_code

    def view_accounts(self):
        with sql.connect('accounts.db') as conn:
            cur = conn.cursor()
            id_sercher = cur.execute("""SELECT id FROM users WHERE user_name =? and user_lastname =?""",
                                     (self.user_name, self.user_lastname))

            accounts_sercher = cur.execute("""SELECT * FROM accounts WHERE id_user =?""",
                                           (id_sercher.fetchall()[0]))
            print(accounts_sercher.fetchall())

    def open_accounts(self):
        with sql.connect('accounts.db') as conn:
            cur = conn.cursor()
            id_sercher = cur.execute("""SELECT id FROM users WHERE user_name =? and user_lastname =?""",
                                     (self.user_name, self.user_lastname))
            type_currency = input("Введите тип счета (Dollar, Pound, Rupe)")
            for id in id_sercher.fetchall():
                if type_currency == 'Dollar':
                    cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Dollar', 0,?)""", id)
                elif type_currency == 'Pound':
                    cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Pound', 0,?)""", id)
                elif type_currency == 'Rupee':
                    cur.execute("""INSERT INTO accounts (currency, score, id_user) VALUES ('Rupee',0,?)""", id)
                else:
                    print('Неизвестный тип счета')
