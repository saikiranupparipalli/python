# class Dish:
#     def __init__(self, name, flavour):
#         self.name = name
#         self.flavour = flavour
#     def orders(self):
#         return  f"{self.name} {self.flavour}"

# select_dish = Dish('chicken', 'spicy')
# print(select_dish)
# print(select_dish.orders())

# inheritance:
class Dish:
    def __init__(self, name, flavour):
        self.name = name
        self.flavour = flavour
    def orders(self):
        return  f"{self.name} {self.flavour}"

class Desert(Dish):
    def __init__(self, name, flavour, desert ):
        super().__init__(name, flavour)
        self.desert  = desert

    def orders(self):
        return f"{self.name} {self.flavour} {self.desert}"
        

  
    
# desert_name = Desert('chicken', 'moderate chilly', 'gulab jamun')
# print(desert_name.desert)

order_li = Desert('chicken', 'moderate chilly', 'gulab jamun')
print(order_li.orders())