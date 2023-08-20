class Series:
    def __init__(self, name: str, year: str, act_list: list, director: str, genre: str, season: int):
        self.__name = name
        self.__year = year
        self.__act_list = act_list
        self.__director = director
        self.__genre = genre
        self.__season = season

    def show(self):
        print(
            f'Название сериала: {self.__name}\nГод: {self.__year}\nСписок актёров: {self.__act_list}\n'
            f'Режисёр: {self.__director}\nЖанр: {self.__genre}\nКол-во сезонов: {self.__season}')

    @property
    def name(self):
        return self.__name
