my_dict = {}
my_dict={'john':{
    "name":"John",
    "age":30,
    "city":"New York",
    "group":'student',
    "department":'devops',
    "course":'python',
    "result":'pass'
},
'peter':{
    "name":"Peter", 
    "age":40,
    "city":"Boston",
    "group":'student',
    "department":'devops',
    "course":'python',
    "result":'fail'
}}

print('-'*100)


class Bil:
    def __init__(self,model,year,color='black'):
        self.model = model
        self.year = year
        self.color = color

    def bil_info(self):
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Color: {self.color}')
    def __str__(self):
        return f'{self.model} {self.year} {self.color}'
    
# class Toyota inherits from Bil
class Toyota(Bil):
    def __init__(self,brand,model,year,color='black'):
        super().__init__(model,year,color)
        self.brand = brand
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.color}'
    
# class Volvo inherits from Bil
class Volvo(Bil):
    def __init__(self,brand,model,year,color='black'):
        super().__init__(model,year,color)
        self.brand = brand
    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.color}'
    
# class BMW inherits from Bil
class BMW(Bil):
    def __init__(self,brand,model,year,color='black'):
        super().__init__(model,year,color)
        self.brand = brand
    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.color}'