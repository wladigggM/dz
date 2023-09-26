import sqlite3 as sql


def counts_games_sercher(name_list: list):
    for name in name_list:
        res = cur.execute(f"""
        SELECT name, count(id) FROM games WHERE name = '{name}'
        """)
        print(res.fetchall())


def total_scores_games_sercher(name_list: list):
    for name in name_list:
        res = cur.execute(f"""
    SELECT name, sum(score) FROM games WHERE name = '{name}'
    """)
        print(res.fetchall())


def total_games_sercerh():
    res = cur.execute(f"""
    SELECT count(id) FROM games
    """)
    print(res.fetchall())


def bad_scores_sercher(name_list: list):
    for name in name_list:
        res = cur.execute(f"""
    SELECT name, min(score) FROM games WHERE name = '{name}'
    """)
        print(res.fetchall())


with sql.connect('newDB.db') as conn:
    cur = conn.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS games;
    DROP TABLE IF EXISTS players;
    
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        best_score INTEGER NOT NULL);
        
    CREATE TABLE IF NOT EXISTS games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        id_player INTEGER NOT NULL,
        FOREIGN KEY (id_player) REFERENCES players (id));
    
    INSERT INTO players (name, best_score) VALUES 
        ('Миша',200),
        ('Ваня',154),
        ('Дима',178),
        ('Коля',210);
        
    INSERT INTO games (name, score, id_player) VALUES 
        ('Миша',110,1),
        ('Миша',200,1),
        ('Дима',178,3),
        ('Коля',10,4),
        ('Коля',30,4),
        ('Коля',40,4),
        ('Ваня',154,2),
        ('Коля',210,4);
        """)
    while True:
        choice = int(input("""
        1.Показать игроков и кол-во сыгранных ими игр
        2.Показать игроков и их итоговый счет за все сыгранные игры
        3.Найти общее кол-во игр
        4.Найти худший результат у каждого игрока
        5.Выход
        """))
        name_list = ['Миша', 'Ваня', 'Дима', 'Коля']
        if choice == 1:
            counts_games_sercher(name_list)
        elif choice == 2:
            total_scores_games_sercher(name_list)
        elif choice == 3:
            total_games_sercerh()
        elif choice == 4:
            bad_scores_sercher(name_list)
        elif choice == 5:
            break
