num = int(input())
if num % 10 == 1:
    print(num, 'попугай')
elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
    print(num, 'попугая')
else:
    print(num, 'попугаев')
