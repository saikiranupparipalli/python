# static method
class Rent_house:
    def __init__(self, colony, price):
        self.colony = colony
        self.price = price
    @staticmethod
    def get_details( owner):
        # self.owner = owner
        # return self.owner
        return owner
search = Rent_house('balajinagar', 6500)
print(search.get_details('saikiran'))