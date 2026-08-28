class car:
    def __init__(self, model="", year=0, maker="", engine=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.maker = maker
        self.engine = engine
        self.color = color
        self.price = price

    def __str__(self):
        return f"модель: {self.model}, год: {self.year}, производитель: {self.maker}, двигатель: {self.engine}, цвет: {self.color}, цена: {self.price}"

    def input_data(self):
        self.model = input("введите модель: ")
        self.year = input("введите год выпуска: ")
        self.maker = input("введите производителя: ")
        self.engine = input("введите объем двигателя: ")
        self.color = input("введите цвет: ")
        self.price = input("введите цену: ")

    def update_price(self, new_price):
        self.price = new_price

my_car = car("rio", 2020, "kia", 1.6, "black", 15000)
print(my_car)