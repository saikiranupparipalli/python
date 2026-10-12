# create a class with attributes like brand, model. create an instance of this class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

myCar = Car('BMW', 'gls 560')
print(myCar.brand, myCar.model)
print(myCar.full_name())