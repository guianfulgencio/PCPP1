class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter +=1

    def walk(self):
        pass

    def quack(self):
        print('quacks')

class Chicken:
    species = 'chicken'
    counter = 0

    def __init__(self):
        Chicken.counter +=1

    def walk(self):
        pass

    def cluck(self):
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('How many ducks were born:', Duck.counter)
print('How many chickens were born:', Chicken.counter)

'''print(duckling.species)
print(drake.species)
print(hen.species)
print(Chicken.species)'''

for i in duckling, drake, hen, chicken:
    print('The', i.species, end=' ')
    if i.species == 'duck':
        i.quack()
    elif i.species == 'chicken':
        i.cluck()
