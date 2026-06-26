class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
class Car(Transport):
    def __init__(self, name, speed, kpp):
        super().__init__(name, speed)
        self.kpp = kpp
class Bus(Transport):
    def __init__(self, name, speed, konduktor):
        super().__init__(name, speed)
        self.konduktor = konduktor
class Plane(Transport):
    def __init__(self, name, speed, krilya):
        super().__init__(name, speed)
        self.krilya = krilya
    def fly(self):
        print('Я ЛЕЧУУУУУУУУУУУУУУУУУУУУУУ')
plane = Plane("Plane", 0.1, 100)
plane.fly()
