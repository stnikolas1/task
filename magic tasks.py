class House():
    def __init__(self, name, number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{str(self.name)}, кол-во этажей: {str(self.number_of_floors)}'

h1 = House('ЖК Горский', 18)
h2 = House ('Домик в деревне', 2)
print(h1)
print(h2)
print(len(h1))
print(len(h2))