""""Convert a function to be a static method.
A static method does not receive an implicit first argument.
To declare a static method, use this idiom:"""
class Bil:
    numb_instance = 0
    type_of_bil = ''
    
    @staticmethod
    def bil_class_info():
        print("This is a static method")
        print('This is Bil class description')


    def __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        Bil.type_of_bil=brand
        Bil.numb_instance += 1

    def __str__(self):
        
        return f"{self.brand} {self.model} {self.year} {self.color} "
    
    def __eq__(self, other):
        if self.brand == other.brand and self.model == other.model and self.year == other.year and self.color == other.color:
            return True
        else:
            return False
        pass
    def bil_info(self):
        
        print(f'{self.brand} {self.model} {self.year} {self.color} {Bil.numb_instance} {Bil.type_of_bil} ')

class Toyota(Bil):
    model_freq = {
        'model': '',
        'frequency': 0
    }
    def __init__(self,brand,model,year,color):
        super().__init__(brand,model,year,color)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
       
    def __str__(self):
         
        return f"{self.brand} {self.model} {self.year} {self.color} "
       
    def __eq__(self, other):
        if self.brand == other.brand and self.model == other.model :
         return True


class Volvo(Bil):   
    model_freq = {
        'model': '',
        'frequency': 0
    }
    def __init__(self,brand,model,year,color):
        super().__init__(brand,model,year,color)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
       
    def __str__(self):
            print(f"{self.brand} {self.model} {self.year} {self.color} ")       
       
    def __eq__(self, other):
      if self.brand == other.brand and self.model == other.model:
        return True



Bil.bil_class_info = staticmethod(Bil.bil_class_info)

Toyota1 = Toyota('Toyota','Corolla',2022 ,'blue')
Toyota1.bil_info()
Toyota1.__eq__(Toyota1)
Toyota2= Toyota('Toyota','Yaris',2024,'blue')
print(Toyota2.__eq__(Toyota2))
Toyota2.bil_info()
Toyota3 = Toyota('Toyota','Corolla',2022 ,'blue')
print(Toyota3.__eq__(Toyota1))
Opel = Bil('Opel','Astra',2020,'black')
Opel.bil_info()
Volvo = Volvo('Volvo','V60',2021,'red')
print(Volvo.__eq__(Volvo))
Volvo.bil_info()
