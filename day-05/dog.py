import animal

DogObject = animal.Animal('Max', 5, 'carnivore')

DogObject.speak('woof')
DogObject.eat()

print(f'Dog name: {DogObject.name}')


