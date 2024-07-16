class Flowers:

    freshness = True

    def __init__(self, type_flower, price, avg_lf_flowers, freshness, long_steam, colour):
        self.type_flower = type_flower
        self.price = price
        self.avg_lf_flowers = avg_lf_flowers
        self.freshness = freshness
        self.long_steam = long_steam
        self.colour = colour

    def __str__(self):
        return f'{self.__class__.__name__} Цветок: {self.type_flower}, ' \
            f'Цена: {self.price}, Срок годности: {self.avg_lf_flowers}, ' \
            f'Длина стебля: {self.long_steam}, Цвет: {self.colour}'


class Rose(Flowers):

    def __init__(self, price, avg_lf_flowers, freshness, long_steam, colour):
        super().__init__('Роза', price, avg_lf_flowers, freshness, long_steam, colour)


class Lyli(Flowers):

    def __init__(self, price, avg_lf_flowers, freshness, long_steam, colour):
        super().__init__('Лилия', price, avg_lf_flowers, freshness, long_steam, colour)


class Orchid(Flowers):

    def __init__(self, price, avg_lf_flowers, freshness, long_steam, colour):
        super().__init__('Орхидея', price, avg_lf_flowers, freshness, long_steam, colour)


class Bouquet:

    def __init__(self):
        self.bouquet = []

    def new_bouquet(self, *obj):
        self.bouquet.extend(obj)

    def print_list(self):
        for i in self.bouquet:
            print(i)

    def price_bouquet(self):
        price_b = [x.price for x in self.bouquet]
        print(sum(price_b))

    def avg_lf(self):
        price_b = [x.avg_lf_flowers for x in self.bouquet]
        print(sum(price_b) / len(self.bouquet))

    def sorted_flowers_price(self):
        self.bouquet.sort(key=lambda x: x.price)
        for flower in self.bouquet:
            print(flower)

    def sorted_fl_name(self):
        self.bouquet.sort(key=lambda x: x.type_flower)
        for flower in self.bouquet:
            print(flower)

    def search_flower(self, y):
        list_flowers = list(filter(lambda x: x.avg_lf_flowers > int(y), self.bouquet))
        for flower in list_flowers:
            print(flower)


fl_rose = Rose(150, 15, True, 120, 'red')
fl_lyli = Lyli(450, 10, True, 150, 'white')
fl_orchid = Orchid(550, 30, True, 110, 'Pink')
fl_rose_1 = Rose(150, 15, True, 120, 'red')
fl_lyli_1 = Lyli(450, 10, True, 150, 'white')
b1 = Bouquet()
b1.new_bouquet(fl_lyli, fl_orchid, fl_rose, fl_rose_1, fl_lyli_1)
b1.sorted_flowers_price()
b1.sorted_fl_name()
b1.search_flower(15)
b1.print_list()
b1.price_bouquet()
b1.avg_lf()
