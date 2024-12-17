from graphics import rect,circ
from graphics.threed import cuboid,sphere
#recctangle module
length=5
breadth=3
print("Area of rectangle: ",rect.area(length,breadth))
print("Perimeter of rectangle: ",rect.perim(length,breadth))
#circle module
r=4
print("Area  of circle:",circ.area(r))
print("Perimeter of circle: ",circ.perim(r))
#cuboid module
l=3
b=7
h=6
print("Surface area of cuboid: ",cuboid.surarea(l,b,h))
print("Perimeter of cuboid: ",cuboid.perim(l,b,h))
#sphere module
r=7
print("Surface area of sphere: ",sphere.surarea(r))
print("Perimeter of cuboid: ",sphere.perim(r))
