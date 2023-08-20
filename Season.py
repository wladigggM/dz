class Season:
    def __init__(self, name, quant_series, list_series):
        self.__name = name
        self.__quant_series = quant_series
        self.__list_series = list_series

    def show(self):
        print(f'Название: {self.__name}\nКол-во серий: {self.__quant_series}\nСписок серий: {self.__list_series}\n')

    @property
    def name(self):
        return self.__name

    @property
    def quant_s(self):
        return self.__quant_series

    @property
    def list_s(self):
        return self.__list_series
