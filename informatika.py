from math import sqrt
x1,y1=map(int, input("Координаты 1 точки: ").split())
x2,y2=map(int, input("Координаты 2 точки: ").split())

if sqrt(x1**2 + y1**2) < sqrt(x2**2 + y2**2):
    print('Точка 1 ближе к началу координат.')
else:
    print('Точка 2 ближе к началу координат.')




