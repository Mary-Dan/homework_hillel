import random
class Car:
    """Оголошуємо клас Car для представлення автомобілів"""
    def __init__(self, model, color):
        self.model = model
        self.color = color
        # повертаємо випадкове число, яке буде в нас за пальне
        self.fuel = random.randrange(0,9)
        # створюємо початкову шкидкість авто
        self.trip_distance = 0

    def move(self, distance):
        # створюємо метод для переміщення автомобілів
        if self.fuel >= distance:
            self.trip_distance += distance
            self.fuel -= distance
        else:
            self.trip_distance += self.fuel
            self.fuel = 0

    def __result__(self):
        return f"Car {self.model} ({self.color}) - Trip Distance: {self.trip_distance} km, Fuel: {self.fuel} liters"

car1 = "Nissan", "green"
car2 = "BMW", "black"
car3 = "VAZ-2101", "white"

# задаємо бажану швидкість під час гонки
desired_dist = 100
dist = 0

while dist < desired_dist:
    for car in [car1, car2, car3]:
        distance = random.randrange(0, 9)
        car.move(distance)
        dist += distance

# Знаходимо переможця на основі максимальної пройденої відстані
winner = max([car1, car2, car3], key=lambda x: x.trip_distance)

print(f"{winner.model} переміг! Проїхав {winner.trip_distance} км.")