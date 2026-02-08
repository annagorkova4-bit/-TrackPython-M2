# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC
import doctest

class Furniture(ABC):
    """
    Документация на класс.
    Класс описывает предметы мебели.
    """
    def __init__(self, material: str, weight: float, color: str):
        """
        Инициализация предмета мебели
        :param material: Материал предмета мебели
        :param weight: Вес предмета мебели в кг
        :param color: Цвет мебели

        Example:
        >>> chair=Furniture("Дерево", 5, "Белый")
        """
        self.material = material
        self.weight = None
        self.init_weight()
        self.color = color
    def init_weight(self, weight):
        """
        Проверка корректности веса.
        """
        if not weight > 0:
            raise TypeError("Вес предмета не может быть отрицательным числом")
        self.weight = weight

    def calculate_cost(self, price: float):
        """
        Расчет стоимости прдемета мебели на основе веса.
        :param price: Цена за метериал
        """
        ...
class Table(Furniture):
    """
        Класс описывает стол, как предмет мебели
    """
    def __init__(self, length: float, width: float, height: float):
        """
        Инициализация стола
        :param length: Длина столешницы в метрах
        :param width: Ширина столешницы в метрах
        :param height: Высота стола в метрах

        Example:
        >>> table = Table(1.5, 0.9, 0.75)
        """
        self.length = None
        self.init_length()
        self.width = None
        self.init_width()
        self.height= None
        self.init_height()
        """
            Проверки корректности размеров стола
        """
    def init_length(self, length):
        if not length > 0:
            raise TypeError("Длина предмета не может быть отрицательным числом")
        self.length = length
    def init_width(self, width):
        if not width > 0:
            raise TypeError("Ширина предмета не может быть отрицательным числом")
        self.width = width
    def init_height(self, height):
        if not height > 0:
            raise TypeError("Высота предмета не может быть отрицательным числом")
        self.height = height

    def TableArea(self):
        """
        Расчет объема занимаемого пространством стола.
        :return: Объем в кубических метрах (length * width * height)

        Examples:
        >>> table = Table(1.0, 0.7, 0.75)
        >>> table.TableArea()
        0.525
        """
        ...
    def SurfaceArea(self):
        """
        Расчет площади столешницы.
        :return: Площадь в квадратных метрах (длина × ширина)

        Examples:
        >>> table = Table(1.8, 1.0, 0.76)
        >>> table.SurfaceArea()
        1.8
        """
        ...
class Wardrobe(Furniture):
    """
    Класс описывает шкаф, как предмет мебели
    """
    def __init__(self, material: str, height: float, shelves_count: int):
        """
        Инициализация шкафа
        :param material: Материал корпуса шкафа
        :param height: Высота шкафа в метрах
        :param shelves_count: Количество полок внутри шкафа

        Examples:
        >>> wardrobe = Wardrobe("сосна", 85.0, 4)
        """
        self.material = material
        self.height = None
        self.shelves_count = shelves_count
        self.init_height()

        def init_height(self, height):
            if not height > 0:
                raise TypeError("Высота предмета не может быть отрицательным числом")
            self.height = height


    def estimate_storage_capacity(self) -> float:
        """
        Оценить вместимость шкафа для хранения вещей.
            :return: Примерная вместимость в кг (на основе объема и количества полок)

        Examples:
        >>> wardrobe = Wardrobe("дуб", 90.0, 6)
        >>> wardrobe.estimate_storage_capacity()
        120.0
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
