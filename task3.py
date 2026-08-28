class stadium:
    def __init__(self, name="", date="", country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"название: {self.name}, дата открытия: {self.date}, страна: {self.country}, город: {self.city}, вместимость: {self.capacity}"

    def input_data(self):
        self.name = input("введите название стадиона: ")
        self.date = input("введите дату открытия: ")
        self.country = input("введите страну: ")
        self.city = input("введите город: ")
        self.capacity = input("введите вместимость: ")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity

my_stadium = stadium("лужники", "1956", "россия", "москва", 81000)
print(my_stadium)