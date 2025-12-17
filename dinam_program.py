#Динамическое программирование
#1
N = int(input('Enter N: ')) 
l = [0,1]
for i in range(0, N-2):
    newel = l[0] + l[1]
    l[0] = l[1]
    l[1] = newel
print(f'Число фибоначи {newel}')
#2
n = int(input('Enter n: '))
p = [1,1,2]
if n > 3:
    for i in range(0, n-3):
        skolko = p[0]+ p[1] + p[2]
        p[0] = p[1]
        p[1] = p[2]
        p[2] = skolko
    print(f'{skolko}')
elif n == 3:
    print(2)
elif n == 2:
    print(1)
elif n == 1:
    print(1)
#3
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1]
]
n = 4
m = 6

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if(i == 0 and j == 0):
            continue
        elif(i == 0 and j != 0):
            coins[i][j] = coins[i][j] + coins[i][j-1]
        elif(i != 0 and j == 0):
            coins[i][j] = coins[i][j] + coins[i-1][j]
        else:
            coins[i][j] = max(coins[i-1][j], coins[i][j-1]) + coins[i][j]
print(coins[-1][-1])
