
class My_Car():
    My_tyres = 4
    def __init__(self,type,color):
        My_Car.My_color = color
        My_Car.My_type = type

    def Color(self, power):
        print(f'My color is  {self.My_color} and power is {power} km/h')

class circle:
    pi = 3.14

    def __init__(self,radius= 1):
        self.area = radius*radius*circle.pi


deepak = My_Car("SUV","black")
print(deepak.My_color)
print(deepak.My_type)
print(deepak.My_tyres)
deepak.Color(180)

mycircle = circle(2)
print(mycircle.area)

print(mycircle.pi)