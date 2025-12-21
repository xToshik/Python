#1
# with open("39762.txt", "r") as f:
#     n = f.readlines()
#     n = [int(el) for el in n]
#
# count = 0
# summa = 0
# for i in range(len(n) - 1):
#     if (n[i] * n[i + 1]) % 15 == 0 and (n[i] + n[i + 1]) % 7 == 0:
#         count += 1
#         if summa < (n[i] + n[i + 1]):
#             summa = (n[i] + n[i + 1])
# print(count, summa)
#2
# with open("68279.txt", 'r') as a:
#     n = a.readlines()
#     n = [int(ele) for ele in n]
#     max_el = 0
#     for elemnt in n:
#         if str(elemnt)[-3:] == "562":
#             if max_el < elemnt:
#                 max_el = elemnt
#
#
# c = 0
# max_sum = 0
# s = []
# for i in range(len(n) - 3):
#     l = [n[i], n[i + 1], n[i + 2], n[i + 3]]
#     l5 = [el for el in l if len(str(el)) == 5]
#     lnot5 = [el for el in l if len(str(el)) != 5]
#     lcrat3 = [el for el in l if el % 3 == 0]
#     lcrat7 = [el for el in l if el % 7 == 0]
#     if len(l5) >= 1 and len(lnot5) >= 2:
#         if len(lcrat3) < len(lcrat7):
#             if sum(l) > max_el and sum(l) < max_el*2:
#                 c += 1
#                 if max_sum < sum(l):
#                     max_sum = sum(l)
# print(c, max_sum)
#Ne rabotaet
# count_four = 0
    # summa_four = 0
    # five = 0
    # kratno_three = 0
    # kratno_seven = 0
    #if len(str(n[i])) == 5 or len(str(n[i+1])) == 5 or len(str(n[i+2])) == 5 or len(str(n[i+3])) == 5:
    # for el in four:
    #     if 10000 < el < 99999:
    #         five += 1
    # ne_five = 4 - five
    # if (five >= 1 and ne_five >= 2):
    #     for x in four:
    #         if (x % 3 == 0):
    #             kratno_three += 1
    #         if (x % 7 == 0):
    #             kratno_seven += 1
    #     if (kratno_three < kratno_seven):
#3
with open("40992.txt", 'r') as file:
    x = file.readlines()
    x = [int(elem) for elem in x]

count = 0
summa = 0
sred = 0
nechet = 0
sum_nechet = 0
for i in x:
    if i % 2 == 1:
        nechet += 1
        sum_nechet += i

sred = sum_nechet / nechet
for i in range(len(x) - 1):
    if (x[i] % 5 == 0 or x[i+1] % 5 == 0) and (x[i] < sred or x[i + 1] < sred):
        count += 1
        if (x[i] + x[i+1]) > summa:
            summa = (x[i] + x[i+1])
print(count, summa)