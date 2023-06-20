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


@pytest.fixture(autouse=True)
def clear_items():
    Item.all = []


@pytest.mark.parametrize(
    ['price', 'quantity', 'total_price'], (
            (10_000, 20, 200_000),
            (1_000, 5, 5_000),
            (1_000, 0, 0),
    )
)
def test_calculate_total_price(price, quantity, total_price):
    item = Item('test_item', price, quantity)
    assert item.calculate_total_price() == total_price


@pytest.mark.parametrize(
    ['discount', 'price_with_discount'], (
            (0, 10_000),
            (0.15, 8_500),
            (0.27, 7_300),
    )
)
def test_apply_discount(discount, price_with_discount):
    item = Item('test_item', 10_000, 20)
    Item.pay_rate = 1 - discount

    item.apply_discount()

    assert item.price == price_with_discount


def test_all_items():
    item1 = Item('test_1', 10_000, 20)
    item2 = Item('test_2', 20_000, 5)

    assert Item.all == [item1, item2]
