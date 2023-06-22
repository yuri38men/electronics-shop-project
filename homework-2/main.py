from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    print(Item.instantiate_from_csv())  # создание объектов из данных файла
    print(len(Item.all))
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
