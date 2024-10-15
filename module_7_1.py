class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open (self.__file_name, 'r') as f:
            read_close = f.read()
            f.close()
            return read_close

    def add(self, *products):
        with open(self.__file_name, 'a') as f:
            for Product in products:
                if Product.name in self.get_products():
                    print(f'Продукт {Product.name} уже есть в магазине')
                    f.close()
                else:
                    f.write(f'\n {print(Product)}')
                    f.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
