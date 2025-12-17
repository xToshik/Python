#x = int(input('Enter x: '))
#y = int(input('Enter y: '))
#if (x <= 8 and y <= 8 and x > 0 and y > 0):
#    if (x % 2 == 0 and y % 2 == 0):
#        print('Черный')
#    elif (x % 2 == 0 and y % 2 == 1):
#        print('Белый')
#    elif (x % 2 == 1 and y % 2 == 1):
#        print('Черный')
#    elif (x % 2 == 1 and y % 2 == 0):
#        print('Белый')
#else:
#    print(f'Нет клетки {x}  {y}')
#1
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
if (x1 <= 8 and y1 <= 8 and x1 > 0 and y1 > 0 and 
x2 <= 8 and y2 <= 8 and x2 > 0 and y2 > 0):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if(dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        print('Конь может попасть с первой клетки на вторую')
    else:
        print('Конь не может попасть с первой клетки на вторую')
else:
    print('Ошибка!')
#2
k = int(input('Enter k: '))
n = int(input('Enter n: '))
while k <= n:
    if (k % 2 == 0):
        print(k)
    k += 1
    
#3
b = 0
while (True):
    number = int(input('Enter number: '))
    if (number == 0):
        break
    else:
        b += number
print(b)
#4
N = int(input('Entet N: '))
a = 1
vivod = 1
while a <= N:
    vivod = vivod * a
    a += 1
print(f'Факториал числа {N} равен {vivod}')
#Динамическое программирование
