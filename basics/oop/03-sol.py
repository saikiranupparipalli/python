# encapsulation
class Study_material:
    def __init__(self, sm_name, price):
        self.sm_name = sm_name
        self.__price = price
    def get_price(self): 
        # getter method which is used for encapsulation
        return self.__price
class Minfo(Study_material):
    def __init__(self, sm_name, price, syllabus):
        super().__init__(sm_name, price)    
        self.syllabus = syllabus
    def cp(self):
        return f"{self.sm_name}, {self.price}, {self.syllabus}"

record = Study_material('BEE', 649)
record2 = Minfo('Applied physics', 857, 'newtons third law complete module')

# print(record2.price)
# print(record.get_price())