class Battery:
    def battery_info(self):
        return 'this is battery info'
class Engine:
    def engine_info(self):
        return 'this is engine info'

class Electric_car( Battery, Engine):
    pass

details = Electric_car()
print(details.battery_info())

# multi-inheritence