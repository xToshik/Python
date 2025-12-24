#1
# mas = []
# mas_15 = []
# a2 = 0
# for x in range(15):
#     a = "123" + f'{x}' + "5"
#     b = "1" + f'{x}' + "233"
#     num1 = int(a, 15)
#     num2 = int(b, 15)
#     objie = num1 + num2
#     if objie % 14 == 0:
#         a1 = objie // 14
#         mas.append(a1)
#         v15 = a1
#         spisok = '0123456789ABCDE'
#         a2 = ''
#         if min(mas) >= a1:
#             while v15 > 0:
#                 a2 = spisok[v15 % 15] + a2
#                 v15 = v15 // 15
#             mas_15.append(a2)
            
# print(min(mas), mas_15)
#2
for p in range(16, 100):
    a = 10*p**6 + 11*p**5 + 2*p**4 + 6*6**3 + 7*p**2 + 13*p**1 + 1
    b = 15*p**6 + 0*p**5 + 2*p**4 + 4*p**3 + 10*p**2 + 8*p**1 + 9
    summa = a + b
    if summa % (p-1) == 0:
        print(p)
#3
# for x in range(0, 9):
#     a = f'{x}' + 'B09'
#     b = f'{x}' + '8E8'
#     num1 = int(a, 17)
#     num2 = int(b, 15)
#     summa = num1 + num2
#     if summa % 155 == 0:
#         print(x)
#4
# spisok ='0123456789AB'
# for x1 in range(0, 11):
#     for y1 in range(0,11):
#         x, y = spisok[x1], spisok[y1]
#         a = int((y + '04' + x + '5'), 11)
#         if x1 < 8 and y1 < 8:
#             b = int(('253' + x + y),8)
#             summa = a + b
#             if summa % 117 == 0:
#                 a1 = summa // 117
#                 print(x, y, a1)
#5
# mas = []
# count = 0
# a = 7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022
# while a > 0:
#     a2 = str(a % 8)
#     mas.append(a2)
#     a = a // 8
# for i in mas:
#     if i == '7':
#         count += 1
# print(count)
