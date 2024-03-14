d1 = int(input())
d2 = int(input())
d3 = int(input())

height = len(set([d1, d2, d3]))

if height == 1:
    print(3)
elif height == 2:
    print(2)
else:
    print(3)
