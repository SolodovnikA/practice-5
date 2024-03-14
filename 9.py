t1, t2, t3 = map(int, input().split())

a = [t1, t2, t3]
mx = max(a)
a.remove(max(a))

print(mx, max(a), min(a))
