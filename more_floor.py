from pdb import runctx


class House():
    def __init__(self, name, number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{str(self.name)}, кол-во этажей: {str(self.number_of_floors)}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        self.number_of_floors = self.number_of_floors +value
        return self

    def __rsub__(self, value):
        self.number_of_floors = self.number_of_floors - value
        if self.number_of_floors >= 1:
            return self
        else:
            print('При вычитании получается 0 этажей')

    def __rmul__(self, value):
        if value == 0:
            print('Нельзя умножать на 0 этажей')
        else:
            self.number_of_floors = self.number_of_floors * value
            return self

    def __sub__(self, value):
        self.number_of_floors = self.number_of_floors - value
        if self.number_of_floors >= 1:
            return self
        else:
            print('При вычитании получается 0 этажей')

    def __mul__(self, value):
        if value == 0:
            print('Нельзя умножать на 0 этажей')
        else:
            self.number_of_floors = self.number_of_floors * value
            return self

    def __isub__(self, value):
        self.number_of_floors = self.number_of_floors - value
        if self.number_of_floors >= 1:
            return self
        else:
            print('При вычитании получается 0 этажей')

    def __imul__(self, value):
        if value == 0:
            print('Нельзя умножать на 0 этажей')
        else:
            self.number_of_floors = self.number_of_floors * value
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__