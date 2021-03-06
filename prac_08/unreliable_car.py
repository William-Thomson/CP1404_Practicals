from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{} Car has {} reliability.".format(super().__str__(),
                                                   self.reliability)

    def drive(self, distance):
        if self.reliability > randint(0, 100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven


def test_unreliable_car():
    new_car = UnreliableCar('Hyundai', 100, 80)
    new_car.drive(50)
    print(new_car)


test_unreliable_car()
