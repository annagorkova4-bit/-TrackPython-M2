if __name__ == "__main__":
    # Write your solution here
    class Building:
        """Базовый класс здания"""
        def __init__(self, address: str, floors: int, year_built: int):
            """
            Конструктор базового класса.

            :param address: Адрес здания
            :param floors: Количество этажей
            :param year_built: Год постройки
            """
            self.address = address
            self.floors = floors
            self.year_built = None
            self.init_year(year_built)

        _current_year = 2026 # Константа внутри класса для проверки года.
        def init_year(self, year_built):
            """Проверка корректности года"""
            if year_built > Building._current_year:
                raise ValueError (f'Год постройки {year_built} не может быть больше текущего года {Building._current_year}')
            else:
                self.year_built = year_built

        def floors_info(self) -> str:
            """Классификация здания по этажности"""
            if self.floors <= 4:
                return "Малоэтажное здание"
            elif self.floors <= 9:
                return "Многоэтажное здание"
            elif self.floors <= 20:
                return "Здание повышенной этажности"
            else:
                return "Высотное здание"

        def __str__(self) -> str:
            return f'Адрес здания: "{self.address}", {self.floors} эт., {self.year_built} г. постройки'

        def __repr__(self) -> str:
            return f'Building("{self.address}", {self.floors}, {self.year_built})'

    class House(Building):
        """Дочерний класс: ИЖС"""
        def __init__(self, address: str, floors: int, year_built: int, rooms: int, area: int, garage: bool):
            """
            Конструктор дочернего класса.

            :param address: Адрес здания
            :param floors: Количество этажей
            :param year_built: Год постройки
            :param rooms: Количество комнат
            :param area: Площадь
            :param garage: Наличие гаража
            """
            super().__init__(address, floors, year_built)
            self.rooms = rooms
            self.area = area
            self.garage = garage

        def floors_info(self) -> str:
            """
            Перегруженный метод классификации здания по этажности.
            Причина: Для частных жилых домах количество этажей не должно превышать 3.
            """
            if self.floors == 1:
                return "Одноэтажный дом"
            elif self.floors == 2:
                return "Двухэтажный дом"
            elif self.floors == 3:
                return "Трехэтажный дом (включая мансарду)"
            else:
                return "Частное домостроение в России, согласно Градостроительному кодексу РФ, ограничивается максимум 3 надземными этажами"

        def __str__(self) -> str:
            """Перегруженный метод __str__ для дома"""
            if self.garage:
                garage_text = "есть гараж"
            else:
                garage_text = "без гаража"
            return (f'Адрес дома: "{self.address}", {self.floors} эт., {self.year_built} г. постройки, '
                    f'{self.rooms} комнат, {self.area} м2, {garage_text}.')

        def __repr__(self) -> str:
            """Перегруженный метод __repr__ для дома"""
            return (f'House("{self.address}", {self.floors}, {self.year_built},'
                    f'{self.rooms}, {self.area}, {self.garage})')


#Тест
    B = Building("ул. Ленина, д. 10", 25, 2005)
    H = House("ул. Мира, д. 45", 2, 2012, 4, 445, True)

    print("=== Базовый класс Building ===")
    print(B)
    print(f"Этажность: {B.floors_info()}")
    print(repr(B))

    print("\n=== Дочерний класс House ===")
    print(H)
    print(f"Этажность: {H.floors_info()}")
    print(repr(H))

    pass
