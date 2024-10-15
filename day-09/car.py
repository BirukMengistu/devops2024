class Car:      
    def __init__(self,make,brand,model,year,price):
        self.make = make
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.started= False
        self.speed = 0
        self.max_speed = 100
    # ....

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False

    def acceleration(self ,value):
        if not self.started:
            print('The car is not started')
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f'The car is moving at {self.speed} km/h')
    def brake(self,value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f'The car is moving at {self.speed} km/h')

    def __str__(self):
        return f"{self.make} {self.brand} {self.model} {self.year} {self.price} {self.speed} {self.max_speed} {self.started} "