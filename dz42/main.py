# Функционал можно было реализовать лучше, но к сожалению ограничен по времени :(

from db import *
from classes import *

while True:
    create_account_table()
    choice = input("""Введите пункт меню: 
    1. Добавить пользователя
    2. Открытие счета
    3. Просмотр учетных записей
    4. Выход из программы
    """)

    if choice == '1':
        user_name = input('Введите имя пользователя: ')
        user_lastname = input('Введите фамилию пользователя: ')
        mail_code = input('Введите почтовый код пользователя: ')
        create_account(user_name, user_lastname, mail_code)
        user = User(user_name, user_lastname, mail_code)

        while True:
            choice = input("""Введите пункт меню: 
            1. Просмотреть счета
            2. Открыть новый счет
            3. Выход
            """)
            if choice == '1':
                user.view_accounts()
            elif choice == '2':
                user.open_accounts()
            elif choice == '3':
                break

    elif choice == '2':
        user_name = input('Введите имя пользователя: ')
        user_lastname = input('Введите фамилию пользователя: ')
        type_currency = input('Введите тип счета (Dollar, Pound, Rupee): ')
        open_account(user_name, user_lastname, type_currency)

    elif choice == '3':
        view_accounts()
    elif choice == '4':
        break
