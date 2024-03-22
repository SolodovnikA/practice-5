import turtle as t

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

t.pu()
t.goto(xc, yc)
t.pd()
t.circle(r)

t.pu()
t.goto(x, y)
t.pd()
t.dot(3)

d = ((x-xc)**2 + (y-yc)**2)**0.5
if d < r:
    t.write('Точка внутри окружности')
elif d > r:
    t.write('Точка вне окружности')
