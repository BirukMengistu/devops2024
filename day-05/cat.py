import animal

CatObject = animal.Animal('Tom', 3, 'carnivore')
CatObject.speak('meow')
CatObject.eat()
print(f'Cat name: {CatObject.name}')