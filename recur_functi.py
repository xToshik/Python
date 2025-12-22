# cook your dish here
#1
# def factorial(n):
#     otvet = 1
#     a = 1
#     if n >= 1:
#         while a <= n:
#             otvet = otvet * a
#             a += 1
#     return otvet
    
# n = int(input('Enter n: '))
# print(factorial(n))
#2
# def remove_vowels(string):
#     udarnie = "aeiouy"
#     udarnie_spisok = ['a', 'e', 'i', 'o', 'u', 'y']
#     otvet = []
#     for i in string:
#         if i not in udarnie_spisok:
#             otvet.append(i)
#     return otvet
    
# print(remove_vowels('apple'))
# print(remove_vowels('orange'))
#3
# def pascal(n):
#     spisok_treugonik = [1]
#     if n >= 0:
#         for i in range(1, n):
#             spisok_treugonik.append(spisok_treugonik[-1] * (n - i) // i)
#         return spisok_treugonik
#     else:
#         return 0
# print(pascal(5))
# print(pascal(-1))
#final boss
# def solve(maze):
#     print(maze)
#     count = 0
#     for i in range(len(maze)):
#         for j in range(len(maze[i])):
#             if maze[i][j] == 'S':
#                 sx, sy = i, j
    
#     while True:
        
# maze = [
#     'S----',
#     '##---',
#     '---##',
#     '----X'
# ]

# print(solve(maze))

def solve(maze):
    print(maze)
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == '-'and j < 6):
                if (maze[i+1][j] == '#'):
                    print('Right')
                elif maze[i][j] == '-':
                    print('right')
            elif(maze[i][j] == '-'):
                print('Down')
    print(count)
    
maze = [
    'S----',
    '##---',
    '---##',
    '----X'
]

print(solve(maze))