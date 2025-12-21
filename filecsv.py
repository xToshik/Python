import csv
#1
# with open('36031.csv', 'r') as f:
#     n = list(csv.reader(f))
#     l = []
#     for i1 in range(len(n) - 1):
#         a = (n[i1][0].split(';'))
#         a = [int(el) for el in a]
#         l.append(a)
#     print(l)
# count = 0
# s = [t[::-1] for t in l[::-1]]
# n = 0
# m = 0
# for i in range(len(s)):
#     n += 1
#     for j in range(len(s[i])):
#         if(i == 0 and j == 0):
#             m += 1
#             s[i][j] = s[i][j]
#             continue
#         elif(i == 0):
#             s[i][j] = s[i][j] + s[i][j-1]
#             m += 1
#         elif (j == 0):
#             s[i][j] = s[i][j] + s[i-1][j]
#         else:
#             if s[i-1][j] >= s[i][j-1]:
#                 s[i][j] = s[i-1][j] + s[i][j]
#             else:
#                 s[i][j] = s[i][j - 1] + s[i][j]
# print(s[-1][-1])
# print(n, m)
# new_mas =[]
# j, j = n -1, m -1
# while i > 0 or j > 0:
#     if i == 0:
#         new_mas.append('L')
#         j -= 1
#     elif j == 0:
#         new_mas.append('U')
#         i -= 1
#     else:
#         if s[i-1][j] > s[i][j-1]:
#             new_mas.append('U')
#             i -= 1
#         else:
#             new_mas.append('L')
#             j -= 1
# print(f' {",".join(new_mas)}')
#2
with open('59778.csv', 'r') as f:
    n = list(csv.reader(f))
    l = []
    for i1 in range(len(n) - 1):
        a = (n[i1][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
count = 0
four_num = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i].count(l[i][j]) == 4:
            repeat = l[i][j]
            x = []
            for j in range(len(l[i])):
                if l[i][j] not in x and l[i][j] != repeat:
                    x.append(l[i][j])
            summa_repeat = 4 * repeat
            average_sum = sum(x) / 3
            if average_sum > summa_repeat:
                count += 1
print(count//4)
#3
with open("29666.csv", 'r') as file:
    n = csv.reader(file, delimiter =';')
    num = []
    for row in n:
        num.extend([float(x.replace(',', '.')) for x in row])

max_sum = num[0]
for i in range(len(num)):
    summa = num[i]
    max = num[i]
    for j in range(i+1, len(num)):
        if num[j] < num[j-1]:
            summa += num[j]
            if summa > max:
                max = summa
        else:
            break
    if max > max_sum:
        max_sum = max

print(max_sum)