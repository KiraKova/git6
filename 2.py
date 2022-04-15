class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_square_c(self):
        return self.width / 6.5 + 0.5

    @property
    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_square_full(self):
        return str(f'Площадь ткани равна {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто потребуется {self.square_c}'


class Suit(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм потребуется {self.square_s}'


coat = Coat(5, 6)

print(coat)
print(coat.get_square_c)
print(coat.get_square_full)

suit = Suit(4, 2)
print(suit)
print(suit.get_square_s)
print(suit.get_square_full)



