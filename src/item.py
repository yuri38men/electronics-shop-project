import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print(name[:10])

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join('.', 'src', 'items.csv')
        try:
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.all.append(row)
                return cls.all
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')
        except InstantiateCSVError:
            raise InstantiateCSVError('Файл items.csv поврежден')

    @staticmethod
    def string_to_number(string_value):
        return int(string_value)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл items.csv поврежден"):
        super().__init__(message)
