class Car:

    def move(self):
        print("Car is driving")

class Plane:

    def move(self):
        print("Plane is flying")

vehicles = [Car(), Plane()]

for vehicle in vehicles:
    vehicle.move()
