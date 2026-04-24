from basic_programs.mypack.basicshape import areaofsquare
from basic_programs.mypack.basicshape import perimeterofsquare
from basic_programs.mypack.basicshape import areaofrect
from basic_programs.mypack.basicshape import perimeterofrect
from basic_programs.circle import areaofcircle, perimeterofcircle

radius = int(input('Enter Radius'))

print('Area : ', areaofcircle(rad=radius))
print('Peri : ', perimeterofcircle(rad=radius))

si = int(input('Enter Side of Square'))
print('Area : ', areaofsquare(side=si))
print('Peri : ', perimeterofsquare(side=si))

l = int(input('Enter Side of Square'))
b = int(input('Enter Side of Square'))
print('Area : ', areaofrect(l,b))
print('Peri : ', perimeterofrect(l,b))





























