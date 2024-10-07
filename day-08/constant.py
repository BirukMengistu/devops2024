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
    def __init__(self,brand,model,year,color='black'):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def bil_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Color: {self.color}')