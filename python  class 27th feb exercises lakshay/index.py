class Car:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year
    def printCarDetails(self):
        print(f'car Details: Model: {self.model} Make: {self.make} Year: {self.year}')

car1 = Car("vitz","toyota","2017")
car1.printCarDetails()


for i in range(1,10):
    if i % 2 ==0:
        print(f'{i} is even')
    elif i % 3 ==0:
        print(f'{i} is multiple of 3')
    else:
        print(f'{i} is neither multiple of 2 or 3')
