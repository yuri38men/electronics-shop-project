import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import Keyboard


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


def test_string_to_number():
    string_value = '5'
    assert Item.string_to_number(string_value) == 5


def test_negative_string_to_number():
    string_value = '-10'
    assert Item.string_to_number(string_value) == -10


def test_invalid_string_to_number():
    string_value = 'world'
    with pytest.raises(ValueError):
        Item.string_to_number(string_value)


def test_name():
    test_name.name = 'Смартфон'
    assert len(test_name.name) < 10
    assert test_name.name == 'Смартфон'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert type(repr(item1)) == str


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_str_1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_repr_1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert type(repr(phone1)) == str


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add():
    item1 = Item("Smartfon", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


class TestKeyboard:
    def test_init(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5, 'EN')
        assert keyboard.name == 'Dark Project KD87A'
        assert keyboard.price == 9600
        assert keyboard.quantity == 5
        assert keyboard.language == 'EN'

    def test_str(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5, 'EN')
        assert str(keyboard) == 'Dark Project KD87A'


def test_error_instantiate_csv_invalid_file():
    try:
        Item.instantiate_from_csv()
    except Exception as e:
        assert str(e) == 'Отсутствует файл items.csv'


def test_instantiate_csv_error():
    error = InstantiateCSVError()
    assert str(error) == "Файл items.csv поврежден"
