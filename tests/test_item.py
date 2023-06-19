"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


class TestItemMethods:
    def test_get_total_price_without_discount(self):
        """
        Создаем экземпляр класса Item с названием,
        ценой и количеством товара
        """
        item = Item("Ноутбук", 20000, 5)

        # проверяем стоимость товара без учета скидки
        assert item.calculate_total_price() == 100000

    def test_get_price_with_discount(self):
        """
        Создаем экземпляр класса Item с названием,
        ценой и количеством товара
        """
        item = Item("Смартфон", 10000, 20)

        # задаем скидку для товара
        Item.pay_rate = 0.8

        # проверяем цену товара с учетом скидки
        assert item.apply_discount() == 8000.0
