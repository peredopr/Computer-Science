def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(5, 6, 7, 8, 9))

class Car():
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.make = kwargs.get('make')

car = Car(make='Nissan', model='GT-R')
print(car.model)