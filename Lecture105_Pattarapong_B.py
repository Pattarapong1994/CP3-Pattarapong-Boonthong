class Vehicle:
    licenseCode = ""
    serialCodr = ""
    def tuneOnAirConditioner(self):
        print("Tune On : Air")

class Cars(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
car1 = Cars()
car1.tuneOnAirConditioner()

pickup1 = Pickup()
pickup1.tuneOnAirConditioner()

van1 = Pickup()
van1.tuneOnAirConditioner()