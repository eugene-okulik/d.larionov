class Flowers:

    freshness = True

    def __init__(self, type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count):
        self.type_flower = type_flower
        self.price = price
        self.avg_lf_flowers = avg_lf_flowers
        self.freshness = freshness
        self.long_steam = long_steam
        self.colour = colour
        self.count = count


class Rose(Flowers):

    def __init__(self, type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count):
        super().__init__(type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count)

    def print_rose(self):
        if self.freshness is True:
            print(
                'Цветок: {}, Цена: {}, средник срок жизни цветка: {}, Свежие, длина стебля: {}, цвет: {}, кличество: {}'
                .format(self.type_flower, self.price, self.avg_lf_flowers, self.long_steam, self.colour, self.count)
            )


class Lyli(Flowers):

    def __init__(self, type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count):
        super().__init__(type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count)

    def print_lyli(self):
        if self.freshness is True:
            print(
                'Цветок: {}, Цена: {}, средник срок жизни цветка: {}, Свежие, длина стебля: {}, цвет: {}, кличество: {}'
                .format(self.type_flower, self.price, self.avg_lf_flowers, self.long_steam, self.colour, self.count)
            )


class Orchid(Flowers):
    def __init__(self, type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count):
        super().__init__(type_flower, price, avg_lf_flowers, freshness, long_steam, colour, count)

    def print_orchid(self):
        if self.freshness is True:
            print(
                'Цветок: {}, Цена: {}, средник срок жизни цветка: {}, Свежие, длина стебля: {}, цвет: {}, кличество: {}'
                .format(self.type_flower, self.price, self.avg_lf_flowers, self.long_steam, self.colour, self.count)
            )


class Bouquet:

    def __init__(self, count_rose, count_lyli, count_orchid):
        self.count_rose = count_rose
        self.count_lyli = count_lyli
        self.count_orchid = count_orchid
        self.object = [flower_rose, flower_orchid, flower_lily]

    def print_object(self):
        list_object = [flower_rose.price, flower_lily.price, flower_orchid.price]
        return list_object

    def print_long_steam(self):
        list_steam = [flower_rose.long_steam, flower_lily.long_steam, flower_orchid.long_steam]
        return list_steam

    def price_bouquet(self):
        print(flower_rose.price * flower_rose.count
            + flower_lily.price * flower_lily.count
            + flower_orchid.price * flower_orchid.count)

    def life_bouquet(self):
        lf_b = (flower_rose.avg_lf_flowers + flower_lily.avg_lf_flowers + flower_orchid.avg_lf_flowers) / 3
        print(round(lf_b))

    def sortet_flowers(self):
        while True:
            question = int(input(
                            "'Введите значение сортировки цетов в букете:\n"
                            " 1 - сортировка по цвету\n"
                            " 2 - сортировка по длине стебля\n"
                            " 3 - сортировка по стоимости'\n"))
            if question == int(1):
                print(flower_rose.colour, bouquet.count_rose, flower_lily.colour,
                       bouquet.count_lyli, flower_orchid.colour, bouquet.count_orchid)
            elif question == int(2):
                print(flower_rose.type_flower, flower_rose.long_steam, flower_lily.type_flower,
                      flower_lily.long_steam, flower_orchid.type_flower, flower_orchid.long_steam)
            elif question == int(3):
                print(flower_rose.type_flower, flower_rose.price, flower_lily.type_flower,
                      flower_lily.price, flower_orchid.type_flower, flower_orchid.price)
            break

    def search_flower(self):
        while True:
            question = int(input(
                            "'Введите значение поиска цетов в букете:\n"
                            " 1 - поиск по стоимости\n"
                            " 2 - сортировка по длине стебля\n"))
            if question == int(1):
                qe = int(input('Введите желаемую стоимость: '))
                if qe > 150:
                    print(list(filter(lambda x: x > 150, bouquet.print_object())))
                elif qe <= 150:
                    print(list(filter(lambda x: x <= 150, bouquet.print_object())))
            elif question == int(2):
                lo = int(input('Введите желаемую длину цвтека: '))
                if lo > 120:
                    print(list(filter(lambda x: x > 120, bouquet.print_long_steam())))
                elif lo <= 120:
                    print(list(filter(lambda x: x < 120, bouquet.print_long_steam())))
            break


flower_rose = Rose('Роза', 150, 21, True, 120, 'red', 5)
flower_lily = Lyli('Лилия', 450, 15, True, 125, 'blue', 5)
flower_orchid = Orchid('Орхидея', 550, 22, True, 150, 'white', 5)
flower_rose.print_rose()
flower_orchid.print_orchid()
flower_lily.print_lyli()
bouquet = Bouquet(5, 5, 5)
bouquet.price_bouquet()
bouquet.life_bouquet()
bouquet.sortet_flowers()
bouquet.search_flower()
