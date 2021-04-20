class Minhalista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, item):
        return self.__items[item]

    def __setitem__(self, key, value):
        self.__items[key] = value

    def __delitem__(self, key):
        del self.__items[key]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()



lista = Minhalista()
lista.add("Renan")
lista.add("Maria")
lista.add("Ivan")

print(lista)
print(lista[0])
lista[0] = "Joao"

del lista[0]

for i in lista:
    print(i)

print(lista)
print(lista[0])