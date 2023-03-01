'''class Demo:
    class_var = 'shared variable'
    
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

print(Demo.class_var)
print(Demo.__dict__)
'''

temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")
else:
    print("Zero")
