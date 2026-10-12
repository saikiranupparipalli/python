# property decorator
class Showroom:
    def __init__(self, name, model):
        self.name = name
        self.__model = model
    @property
    def get_model(self):
        return self.__model
info = Showroom('harley', 2009)
print(info.get_model)
# property decorator gives the previlage to access the function directly with properties

print(isinstance(info, Showroom))
# ininstance 