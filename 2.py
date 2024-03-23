xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

a = 'Точка внутри окружности'
b = 'Точка вне окружности'

import turtle as t

t.pu()
t.goto(xc, yc)
t.pd()
t.circle(r)

t.pu()
t.goto(x, y)
t.pd()
t.dot(10)

t.pu()
t.goto(x - 20, y - 20)
t.pd()

d = ((x - xc)**2 + (y - yc)**2)**0.5
if d < r:
    t.write(a)
elif d > r:
    t.write(b)
