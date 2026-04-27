from oopconcepts.rectangle import Rectangle
from oopconcepts.square import Square

sqobj = Square(10)

print('Square')
print(f'Area: {sqobj.calculate_area()} \t Perimeter: {sqobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)
print('Rectangle')
print(f'Area: {rectobj.calculate_area()} \t Perimeter: {rectobj.calculate_perimeter()}')

