class Flower:
    name: str
    price: float
    freshness_days: int
    stem_length: float
    color: str

    def __init__(self, name: str, price: float, freshness_days: int, stem_length: float, color: str):
        self.name = name
        self.price = price
        self.freshness_days = freshness_days
        self.stem_length = stem_length
        self.color = color

    def __str__(self):
        return f"{self.name}(цена={self.price}, свежесть={self.freshness_days} дней)"

    def __repr__(self):
        return f"{self.name}(цена={self.price}, свежесть={self.freshness_days} дней)"


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


class Bouquet:
    def __init__(self, flowers=None):
        self.flowers = flowers or []

    # Метод добавления цветка в букет
    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    # Определение общей стоимости букета
    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    # Время увядания букета (среднее время жизни цветов)
    def wilt_time(self):
        if not self.flowers:
            return None
        return sum(flower.freshness_days for flower in self.flowers) / len(self.flowers)

    # Методы сортировки цветов в букете
    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness_days, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price, reverse=True)

    # Поиск цветов по параметру среднего времени жизни
    def search_by_freshness(self, min_freshness_days):
        return [
            flower
            for flower in self.flowers
            if flower.freshness_days >= min_freshness_days
        ]


if __name__ == "__main__":
    rose = Rose(name="Роза", price=100, freshness_days=7, stem_length=30, color="красный")
    tulip = Tulip(name="Тюльпан", price=80, freshness_days=5, stem_length=25, color="желтый")
    lily = Lily(name="Лилия", price=120, freshness_days=10, stem_length=40, color="белый")

    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(tulip)
    bouquet.add_flower(lily)

    print("Цветы в букете:", bouquet.flowers)
    print("Общая стоимость букета:", bouquet.total_price())
    print("Среднее время увядания букета:", bouquet.wilt_time(), "дней")

    # Сортировка букета по свежести
    bouquet.sort_by_freshness()
    print("\nОтсортированные по свежести цветы:", bouquet.flowers)

    # Поиск цветов с временем свежести больше 6 дней
    found_flowers = bouquet.search_by_freshness(min_freshness_days=6)
    print("\nЦветы со сроком свежести больше 6 дней:", found_flowers)
